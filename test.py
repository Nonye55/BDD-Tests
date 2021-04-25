from page_objects.pages import TraineeManagement

driver = TraineeManagement()

driver.login()

driver.invite_trainee()
