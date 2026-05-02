import os
from typing import Any

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool


DEFAULT_TO_EMAIL = os.environ.get("DEFAULT_RECIPIENT_EMAIL", "").strip()
DEFAULT_FROM_EMAIL = os.environ.get("SENDGRID_FROM_EMAIL", "").strip()


@function_tool
def send_email(subject: str, html_body: str, to_email: str = "") -> dict[str, Any]:
    api_key = os.environ.get("SENDGRID_API_KEY")
    if not api_key:
        return {"error": "SENDGRID_API_KEY is not set"}

    recipient = (to_email or "").strip() or DEFAULT_TO_EMAIL
    if not recipient:
        return {"error": "No recipient: set DEFAULT_RECIPIENT_EMAIL or pass to_email"}

    if not DEFAULT_FROM_EMAIL:
        return {"error": "SENDGRID_FROM_EMAIL is not set"}

    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    from_email = Email(DEFAULT_FROM_EMAIL)
    to_addr = To(recipient)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_addr, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status_code": response.status_code}


INSTRUCTIONS = """You send a nicely formatted HTML email based on a detailed report.
You will be provided with:
1. The detailed report (and optionally "Recipient email: someone@example.com" at the start).
2. If a recipient email is given, you MUST pass it as the to_email argument when calling send_email; otherwise omit to_email or leave it empty to use the default.
You must use your tool to send one email: convert the report to clean, well-presented HTML and use an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
    handoff_description="Format the research report as HTML and send it by email to the recipient (if provided).",
)
