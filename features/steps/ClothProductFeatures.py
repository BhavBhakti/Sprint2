from behave import *
import logging
from features.pageobjects.product import Product
from features.pageobjects.login import login
from features.pageobjects.search import Search
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

@given(u'we navigate to Flipkart website')
def step_impl(context):
    context.logn = login.fliphome(context)
    log.logger.info("Navigated to Flipkart website")

@given(u'close the window')
def step_impl(context):
    context.logn = login(context.driver)
    context.logn.clickclose()
    log.logger.info("Closed login window")

@given(u'we click on Login Button')
def step_impl(context):
    context.logn = login(context.driver)
    context.logn.clickloginLink()
    log.logger.info("Clicked on Login Button")

@then(u'we give "{numberr}" edit box')
def step_impl(context,numberr):
    context.logn.logmobno(numberr)
    log.logger.info("Entered mobile number")


@then(u'we give the "{passwordd}" edit box')
def step_impl(context,passwordd):
    context.logn.logpassword(passwordd)
    log.logger.info("Entered password")


@then(u'we click on login button')
def step_impl(context):
    context.logn.signinbutton()
    log.logger.info("Clicked SignIn button")


@then(u'type "{search}" in searchbox')
def step_impl(context,search):
    context.s = Search(context.driver)
    context.s.searchbox(search)
    log.logger.info("Entered product to be searched")


@then(u'click on search button')
def step_impl(context):
    context.s.clicksearch()
    log.logger.info("Clicked on search button")


@then(u'click on product image')
def step_impl(context):
    context.pro = Product(context.driver)
    context.pro.clickTop()
    log.logger.info("Clicked on product")


@then(u'switch to window')
def step_impl(context):
    context.pro.winswitch()
    log.logger.info("switched the window")


@then(u'click on all front-back images')
def step_impl(context):
    context.pro.switchimages()
    log.logger.info("Navigated to front-back images of product")


@then(u'Enter "{pincode}"')
def step_impl(context,pincode):
    context.pro.enterpin(pincode)
    log.logger.info("Entered pincode")


@then(u'click on check link')
def step_impl(context):
    context.pro.clickcheck()
    log.logger.info("Clicked on check link")


@then(u'click on all colors')
def step_impl(context):
    context.pro.colour()
    log.logger.info("selected a colour")


@then(u'click on all sizes')
def step_impl(context):
    context.pro.size()
    log.logger.info("selected a size")

@then(u'click on product details')
def step_impl(context):
    context.pro.productplus()
    log.logger.info("Clicked on product details")


@then(u'click on all addtocart')
def step_impl(context):
    context.pro.addtocart()
    log.logger.info("Clicked on add to cart button")

@then(u'verify placeorder button')
def step_impl(context):
    context.pro.placeorder("PLACE ORDER")
    log.logger.info("Verified place order button")


