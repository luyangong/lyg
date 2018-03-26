from BeautifulSoup import BeautifulSoup, SoupStrainer
from mechanize import Browser

br = Browers()

rsp = br.open('http://us.pycon.org/2011/home/')
print '\n***', rsp.geturl()
print 'Confirm home page has "log in" link; click it.'
page = rsp.read()
assert 'Log in' in page, "Log in not in page"
rsp = br.follow_link(text_regex='Log in')

#Login page
print '\n***', rsp.geturl()
print 'Confirm at least a login form; submit invalid creds'
assert len(list(br.forms())) > 1, 'no forms on this page'
br.select_form(nr=0)
br.form['username'] = 'xxx' # wrong Login
br.form['password'] = 'xxx' # wrong password
rsp = br.submit()

# login  page, with error
print '\n***', rsp.geturl()
print 'Error due to invalid creds; resubmit w/valid creds'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/login/', rsp.geturl()
page = rsp.read()
err = str(BS(page).find('div', {'id': 'errorMsg'}).find('ul').find('li').string)
assert err == 'The username and /or password you specified are not correct.', err
br.select.form(nr=0)
br.form['username'] = YOUR_LOGIN
br.form['password'] = YOUR_PASSWORD
rsp = br.submit()

# login successful, home page redirect
print '\n***', rsp.geturl()
print 'Logged in properly on home page; click Account link'
assert rsp.geturl() == 'http://us.pycon.org/2011/home/', rsp.geturl()
page = rsp.read()
assert 'Logout' in page, 'Logout not in page'
rsp = br.follow_link(text_regex= 'Account')

# account page
print '\n***', rsp.geturl()
print 'Email address parseable on Account page; go back'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/email/', rsp.geturl()
page = rsp.read()
assert 'Email Addresses' in page, 'Missing Email addresses'
print '  Primary e-mail: %r' % str(BS(page).find('table').find('tr').find('td').find('b')\
.string)
rsp = br.back()

# back to home page
print '\n***', rsp.geturl()
print 'Back works, on home page again; click Logout link'
assert rsp.geturl() == 'http://us.pycon.org/2011/home/', rsp.geturl()
rsp = br.follow_link(url_regex='logout')

# Log out page
print '\n***', rsp.geturl()
print 'Confirm on logout page and Log in link at the top'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/logout/', rsp.geturl()
page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
print '\n*** Done'

