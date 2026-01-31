import allure
from allure_commons.types import AttachmentType


def add_screenshot(driver):
    allure.attach(
        driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )


def add_logs(driver):
    try:
        logs = driver.get_log("browser")
        text = "\n".join(str(item) for item in logs)
    except Exception as e:
        text = f"Cannot get browser logs: {e}"
    allure.attach(text, name="browser_logs", attachment_type=AttachmentType.TEXT)


def add_html(driver):
    allure.attach(
        driver.page_source,
        name="page_source",
        attachment_type=AttachmentType.HTML
    )


def add_video(session_id: str, selenoid_host: str):
    video_url = f"https://{selenoid_host}/video/{session_id}.mp4"
    html = f"""
    <html>
      <body>
        <p><a href="{video_url}" target="_blank">Open video</a></p>
        <video width="100%" height="100%" controls>
          <source src="{video_url}" type="video/mp4">
        </video>
      </body>
    </html>
    """
    allure.attach(html, name="video", attachment_type=AttachmentType.HTML)
