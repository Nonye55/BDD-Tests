Feature:  Training Management
  As an admin,I should be able to carry-out all administrative duties.

  Background:
    given that I am logged in as an admin


#  Scenario: An Admin can invite a trainee
#    then I should see the Invite Trainees tab
#    when I click on the invite trainees button
#    then I click on the email field
#    when I insert the trainees email address
#    when I click on the add button
#    when I click on the send invites button
#    then I should see a  close button

  Scenario: As an Admin I want create a group
    then I click on the trainees tab
    #then I see the groups tab
    when I click on the groups tab
    then I click on the on the create button
    when I click on the select group field
    when I  select others
    when I click on the groups groups name field
    then I input the groups name
    when I click on the assign course field
    then I select the course
    then I click on the create group button
    then I should see the group created successfully snack bar














