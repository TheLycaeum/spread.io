# Spread.io

[![Build Status](https://travis-ci.org/TheLycaeum/spread.io.svg?branch=master)](https://travis-ci.org/TheLycaeum/spread.io)


-----------Steps to get started on FACEBOOK --------------

1.Go to facebook developer page using below link:-

      https://developers.facebook.com

2. Cick `Log In` Button and login to your facebook account.

3. Cick on `Get started` button and follow the instructions,to
register as a developer.

4. Now you need to create a new app, this is done by selecting `My Apps`.

5. In the app dashboard go to `Settings` --> `Basic`.

6. In order to disable sandbox mode, you will need to fill in
`Display name`, `Contact Email`, `Privacy Policy URL` and save changes.

7. Note: In order to post in timeline, you will have to review your app
by completing `App Review`. and after `App Review` change status of
the app to live. If you are using this application as a personal project
you can managing pages and post on pages where you have
administrive privilage. 

8. Copy `App Id`, `App Secret` and `Display Name` from
`Settings` --> `Basic` and paste in `.config` file --> fields
`client_id`,  `client_secret` and `name` respectively.

9. Add your Page name to which you would like to post in
`.config` file -->  `page_name`.

10. In facebook developer page go to `Tools` --> `Graph API Explorer`
--> `Get Token` --> `Get user access Token`. 

11.Select `publish_pages`, `manage_pages`,
and click on `Get AccessToken`. Give permission to the page you
would like to post on.

12. Open appWindow.py click on `+` --> `Facebook`.
If facebook is disabled skip to Step 16

13. Log into Facebook the first time  with your credentials,
grant permission to the eairlier specified page.

14. Copy `url` and paste on `Enter Pin` field and click ADD.

15. You only need to do Step 12, 13, 14 once every 2 months.

16. Type you mesage on the message box, select `Facebook` from checkbox
and Press Send to send the message.

-------------------Thank You------------------------------
