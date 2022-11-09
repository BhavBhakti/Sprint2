from behave import *
from features.pageobjects.product import Product
from features.pageobjects.login import login

@given(u'we navigate to Flipkart website')
def step_impl(context):
    context.log = login.fliphome(context)

@given(u'close the window')
def step_impl(context):
    context.log = login(context.driver)
    context.log.clickclose()

@given(u'we click on Login Button')
def step_impl(context):
    context.log = login(context.driver)
    context.log.clickloginLink()

@then(u'we give "{numberr}" edit box')
def step_impl(context,numberr):
    context.log.logmobno(numberr)


@then(u'we give the "{passwordd}" edit box')
def step_impl(context,passwordd):
    context.log.logpassword(passwordd)


@then(u'we click on login button')
def step_impl(context):
    context.log.signinbutton()


@then(u'type "{search}" in searchbox')
def step_impl(context,search):
    context.pro = Product(context.driver)
    context.pro.searchbox(search)


@then(u'click on search button')
def step_impl(context):
    context.pro.clicksearch()


@then(u'click on Top image')
def step_impl(context):
    context.pro = Product(context.driver)
    context.pro.clickTop()


@then(u'switch to window')
def step_impl(context):
    context.pro.winswitch()


@then(u'click on all front-back images')
def step_impl(context):
    context.pro.switchimages()


@then(u'Enter "{pincode}"')
def step_impl(context,pincode):
    context.pro.enterpin(pincode)


@then(u'click on check link')
def step_impl(context):
    context.pro.clickcheck()


@then(u'click on all colors')
def step_impl(context):
    context.pro.colour()


@then(u'click on all sizes')
def step_impl(context):
    context.pro.size()

@then(u'click on plus sign')
def step_impl(context):
    context.pro.productplus()


@then(u'click on all addtocart')
def step_impl(context):
    context.pro.addtocart()

@then(u'verify placeorder button')
def step_impl(context):
    context.pro.placeorder("PLACE ORDER")


