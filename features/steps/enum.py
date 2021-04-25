from behave import *
from page_objects.pages import TraineeManagement
from variables import buur

use_step_matcher("re")


@given(u'that I am logged in as an admin')
def step_impl(context):
    context.web = TraineeManagement()
    context.web.login()


# @then(u'I should see the Invite Trainees tab')
# def step_impl(context):
#     context.web.verify(buur.Invite_Trainees, buur.Invite_Trainees_text)
#
#
# @when(u'I click on the invite trainees button')
# def step_impl(context):
#     context.web.click_an_element(buur.invite_button)
#
#
# @then(u'I click on the email field')
# def step_impl(context):
#     context.web.click_an_element(buur.email_field2)
#
#
# @when(u'I insert the trainees email address')
# def step_impl(context):
#     context.web.insert_a_value(buur.email_field2, buur.employees_email)
#
#
# @when(u'I click on the add button')
# def step_impl(context):
#     context.web.click_an_element(buur.add_button)


# @when(u'I click on the send invites button')
# def step_impl(context):
#     context.web.click_an_element(buur.send_invite_button)
#
#
# @then(u'I should see a  close button')
# def step_impl(context):
#     context.web.click_an_element(buur.close_button)


@then(u'I click on the trainees tab')
def step_impl(context):
    context.web.click_an_element(buur.Trainees_tab)


# @then(u'I see the groups tab')
# def step_impl(context):
#     context.web.verify(buur.groups_tab, buur.groups_tab_text)


@when(u'I click on the groups tab')
def step_impl(context):
    context.web.click_an_element(buur.groups_tab)


@then(u'I click on the on the create button')
def step_impl(context):
    context.web.click_an_element(buur.create_button)


@when(u'I click on the select group field')
def step_impl(context):
    context.web.click_an_element(buur.group_field)


@when(u'I  select others')
def step_impl(context):
    context.web.click_an_element(buur.others)


@when(u'I click on the groups groups name field')
def step_impl(context):
    context.web.click_an_element(buur.groups_name_field)


@then(u'I input the groups name')
def step_impl(context):
    context.web.insert_a_value(buur.groups_name_field, buur.groups_name)


@when(u'I click on the assign course field')
def step_impl(context):
    context.web.click_an_element(buur.assign_course_field)


@then(u'I select the course')
def step_impl(context):
    context.web.click_an_element(buur.course_name)


@then(u'I click on the create group button')
def step_impl(context):
    context.web.click_an_element(buur.create_group_button)


@then(u'I should see the group created successfully snack bar')
def step_impl(context):
    pass
