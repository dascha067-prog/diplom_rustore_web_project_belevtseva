import allure
from allure_commons.types import AttachmentType


def add_screenshot(driver):
    png = driver.get_screenshot_as_png()
    allure.attach(
        png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png"
    )


def add_logs(driver):
    log = "".join(f"{text}\n" for text in driver.execute("getLog", {'type': 'browser'})['value'])
    allure.attach(log, "browser_logs", AttachmentType.TEXT, ".log")


def add_html(driver):
    html = driver.page_source
    allure.attach(html, "page_source", AttachmentType.HTML, ".html")


def add_video(session_id: str, selenoid_base_url: str):
    video_url = f"{selenoid_base_url.rstrip('/')}/video/{session_id}.mp4"
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
    allure.attach(html, name="video", attachment_type=allure.attachment_type.HTML)
