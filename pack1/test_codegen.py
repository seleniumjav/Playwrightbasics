import os
import time
from urllib.parse import urljoin

import pytest
from playwright.sync_api import Page, expect


# def test_example(page: Page) -> None:
#     page.goto("https://tutorialsninja.com/demo/")
#     product1=page.locator('.product-layout').filter(has_text="iPhone")
#     product1.locator("button:has-text('Add to Cart')").click()
#     page.wait_for_timeout(3000)


def test_omayo(page:Page):
    page.goto("https://demo.automationtesting.in/Frames.html")
    frame1=page.frame_locator("#singleframe")
    frame1.locator('//input[@type="text"]').fill("python")
    page.wait_for_timeout(3000)

def test_dropdown(page:Page):
    page.goto("https://practice.expandtesting.com/dropdown")
    dropdown=page.locator("#dropdown")
    options=dropdown.locator('option')
    expect(options).to_have_count(3)
    expected_data=[
        ("","Please select an option"),
        ("1","Option 5"),
        ("2","Option 2")
    ]
    for i in range(len(expected_data)):
        expect(options.nth(i)).to_have_text(expected_data[i][1])

    # dropdown.select_option(value="1")

    page.wait_for_timeout(3000)


def test_webtable(page:Page):
    # page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    # table=page.locator('table')
    # rows=table.locator('tr')
    # expect(rows).to_have_count(6)
    #
    #
    # for i in range(rows.count()):
    #     cols=rows.nth(i).locator('td')
    #     if cols.count()>0 and cols.nth(0).inner_text()=="Cierra":
    #         expect(cols.nth(2)).to_have_text("59")
    #
    # page.wait_for_timeout(3000)
    page.goto("https://assertqa.com/practice/webtables")
    table = page.locator('table')
    rows = table.locator('tr')
    expect(rows).to_have_count(6)

    # page.wait_for_timeout(3000)

    for i in range(rows.count()):
        cols = rows.nth(i).locator('td')
        if cols.count() > 0 and cols.nth(1).inner_text() == "John":
            # print(cols.nth(4).inner_text())
            expect(cols.nth(6)).to_have_text("Marketing")


    page.wait_for_timeout(3000)

def test_brokenimage(page:Page):
    page.goto("https://practice.expandtesting.com/broken-images#google_vignette")
    images=page.locator('img')
    broken_images=[]

    for i in range(images.count()):
        src=images.nth(i).get_attribute('src')
        if not src:
            continue
        image_url=urljoin(page.url,src)
        response=page.request.get(image_url)
        if response.status==404:
            broken_images.append(image_url)
    print("number of broken images:",len(broken_images))

    for i in broken_images:
        print("broken image:",i)

def test_tabhandle(page:Page):
    page.goto("https://www.hyrtutorials.com/p/window-handles-practice.html")

    with page.expect_popup() as newtab:
        page.locator("#newTabBtn").click()

    tab1=newtab.value
    tab1.wait_for_load_state()
    assert tab1.url=="https://www.hyrtutorials.com/p/alertsdemo.html"
    print("tab opened")

    page.bring_to_front()
    newtabbtn=page.locator("#newTabBtn")
    expect(newtabbtn).to_be_visible()

def test_calendar(page:Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/date-picker.php")

    expected_year="2028"
    expected_month="April"
    expected_day="28"
    expected_hour="10"
    expected_minute="30"
    expected_time="AM"

    page.locator("#datetimepicker1").click()
    month_input=page.locator('.flatpickr-monthDropdown-months').first
    month_input.click()
    month_input.type(expected_month)
    page.keyboard.press('Enter')

    year_input=page.locator('.numInput.cur-year').first
    year_input.click()
    year_input.type(expected_year)

    page.locator(f"//span[@class='flatpickr-day' and text()='{expected_day}']").first.click()

    hour_input=page.locator('.numInput.flatpickr-hour').first
    hour_input.click()
    hour_input.fill(expected_hour)
    page.wait_for_timeout(3000)

def test_screencast(page:Page):
    page.set_viewport_size({
        "width": 1920,
        "height": 1080
    })

    page.wait_for_timeout(3000)
    page.goto("https://tutorialsninja.com/demo/")

    page.screencast.start(
        path='screencast.webm'
    )

    page.screencast.show_actions(
        position="top-right",
        duration=2000,
        font_size=22
    )

    page.screencast.show_chapter(
        title='Chapter 1',
        description='Tutorialsninja',
        duration=5000
    )

    page.get_by_title("My Account").click(timeout=10000)
    page.get_by_role("link",name="Login").click()
    page.get_by_placeholder("E-Mail Address").fill("seleniumpython@gmail.com")
    page.get_by_placeholder("Password").fill('Selenium@2026')
    page.get_by_role("button",name="Login").click()
    page.screencast.stop()
    page.wait_for_timeout(3000)


@pytest.mark.timeout(60)
def test_slider(page:Page):
    page.goto("https://practice-automation.com/slider/",timeout=4000)
    slider=page.locator("#slideMe")
    expect(slider).to_have_value("25",timeout=4000)
    slider.fill("56")
    page.wait_for_timeout(3000)
    slider.fill("0")

    page.wait_for_timeout(3000)

def test_screenshot(page:Page):
    page.goto("https://tutorialsninja.com/demo/")
    page.screenshot(path='screenshot.png')
    page.wait_for_timeout(3000)

def test_actions(page:Page):
    # page.goto("https://testautomationpractice.blogspot.com/")
    # # page.get_by_role("button",name="Copy Text").click(button="right")
    # page.get_by_role("button",name="Point Me").hover()
    # page.wait_for_timeout(3000)

    page.goto("https://omayo.blogspot.com/")
    page.locator("#checkbox1").uncheck()
    page.wait_for_timeout(3000)
    page.keyboard.press('Tab')

def test_filedownload(page:Page):
    page.goto("https://demo.automationtesting.in/FileDownload.html")
    page.wait_for_timeout(3000)
    with page.expect_download() as downloadinfo:
        page.get_by_role("link",name="Download").first.click()

    download=downloadinfo.value
    download_path=os.path.join(os.getcwd(),download.suggested_filename)
    download.save_as(download_path)
    expected_name='samplefile.pdf'
    assert download.suggested_filename == expected_name

def test_slider1(page:Page):
    page.goto("https://demo.automationtesting.in/Slider.html#google_vignette")
    slider=page.locator("#slider")

    box=slider.bounding_box()
    start_x=box['x']+box['width']/2
    start_y=box['y']+box['height']/2

    page.mouse.move(start_x,start_y)
    page.mouse.down()
    page.mouse.move(
        start_x-100,
        start_y
    )

    page.mouse.up()
    page.wait_for_timeout(3000)

def test_dragndrop(page:Page):
    page.goto("https://demo.automationtesting.in/Static.html")
    src=page.locator("#angular")
    dest=page.locator("#droparea")
    src.drag_to(dest)

    page.wait_for_timeout(3000)

def test_fileupload(page:Page):
    page.goto("https://practice.expandtesting.com/upload")
    with page.expect_file_chooser() as file:
        page.locator('#fileInput').click()

    filevalue=file.value
    filevalue.set_files("C:\\Users\\Admin\\Desktop\\Userdata.csv")
    page.locator("#fileSubmit").click()

    page.wait_for_timeout(3000)