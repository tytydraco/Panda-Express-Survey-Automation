from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def input_survey_code(driver, code, last_digits):
    driver.get("https://www.pandaguestexperience.com/")

    verify_length = code + last_digits
    length_no_spaces = verify_length.replace(" ", "")
    if len(length_no_spaces) != 22:
        raise Exception("Invalid code")

    code_4_digit = code.split(" ")
    for i in range(1, 6):
        input_box = driver.find_element(By.NAME, "CN" + str(i))
        input_box.send_keys(code_4_digit[i - 1])
    input_box = driver.find_element(By.NAME, "CN6")
    input_box.send_keys(last_digits)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "NextButton"))
    )
    next_button.click()

def fill_out_survey(driver, email_addr):
    while True:
        try:
            email_inputs = driver.find_elements(By.NAME, "S000057")
            if email_inputs:
                for email_input in email_inputs:
                    email_input.send_keys(email_addr)
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "NextButton"))
                )
                next_button.click()
                break

            option_buttons = driver.find_elements(By.CLASS_NAME, "radioSimpleInput")
            for i in range(0, len(option_buttons), 5):
                option_buttons[i].click()

            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "NextButton"))
            )
            next_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def main():
    try:
        code = input("Enter panda survey code (put space for '-'): ")
        email_addr = input("Enter email: ")
        last_digits = code[-2:]
        code = code[:-2].replace(" ", "")
        
        service = webdriver.chrome.service.Service('C:\\Program Files (x86)\\chromedriver.exe')
        service.start()
        driver = webdriver.Chrome(service=service)
        
        input_survey_code(driver, code, last_digits)
        fill_out_survey(driver, email_addr)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
