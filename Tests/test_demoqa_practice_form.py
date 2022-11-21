    from Models import controls
    from Models import pages
    from selene.support.conditions import have

    def test_form(open_and_close_form):
        pages.fill_fullname("Andrew", "Vasutenko")
        pages.fill_user_email("qqqqq@qqqq.qq")
        controls.select_gender_male()
        pages.fill_user_number_phone("8800555353")
        controls.fill_date_of_birthday("19 April,1993")
        pages.fill_subjects(("Art", "Commerce"))
        controls.select_hobby_music()
        controls.download_picture()
        pages.fill_curent_adress("Russia,Moscow")
        controls.select_state_and_city("rajasthan", "jaipur")
        controls.submit()

        pages.table_result.should(have.text("Andrew"))
        pages.table_result.should(have.text("Vasutenko"))
        pages.table_result.should(have.text("qqqqq@qqqq.qq"))
        pages.table_result.should(have.text("Male"))
        pages.table_result.should(have.text("8800555353"))
        pages.table_result.should(have.text("19 April,1993"))
        pages.table_result.should(have.text(("Art", "Commerce"))
        pages.table_result.should(have.text("Music"))
        pages.table_result.should(have.text("meme.jpg"))
        pages.table_result.should(have.text("Russia,Moscow"))
        pages.table_result.should(have.text("rajasthan"))
        pages.table_result.should(have.text("jaipur"))

# import os
# from selene.support.shared import browser
# from selene import be, have
#
# first_name = 'Andrew'
# last_name = 'Vasutenko'
# email = 'qqqqq@qqqq.qq'
# mobile_number = '8800555353'
# current_address = 'Earth'
#
#
# def test_demoqa_practice_form():
#     #first page
#     browser.open_url('https://demoqa.com/automation-practice-form')
#     browser.element('#firstName').type(first_name)
#     browser.element('#lastName').type(last_name)
#     browser.element('#userEmail').type(email)
#     browser.element('#gender-radio-1').double_click()
#     browser.element('#userNumber').type(mobile_number)
#     browser.element('#dateOfBirthInput').click()
#     browser.element('.react-datepicker__month-select').type('April')
#     browser.element('.react-datepicker__year-select').type('1993')
#     browser.element('[aria-label="Choose Monday, April 19th, 1993"]').click()
#     browser.element('#subjectsInput').type('Arts').press_enter().type('Commerce').press_enter()
#     browser.element('[for="hobbies-checkbox-1"]').click()
#     browser.element('#uploadPicture').send_keys(os.path.abspath('../Images/meme.jpg'))
#     browser.element('#currentAddress').type(current_address)
#     browser.element('#react-select-3-input').type('rajasthan').press_enter()
#     browser.element('#react-select-4-input').type('jaipur').press_enter()
#     browser.element('#submit').press_enter()
#
#     #second page
#
#     browser.all('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
#     browser.all('.table-responsive').should(have.text(first_name))
#     browser.all('.table-responsive').should(have.text(last_name))
#     browser.all('.table-responsive').should(have.text(email))
#     browser.all('.table-responsive').should(have.text(current_address))
#     browser.all('.table-responsive').should(have.text(mobile_number))
#     browser.all('.table-responsive').should(have.text('meme.jpg'))
#     # browser.all('#closeLargeModal').click() не сработал :(
#     browser.execute_script('document.getElementById("closeLargeModal").click()')