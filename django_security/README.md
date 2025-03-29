# Django Security Practice

## XSS
Cross-Site Scripting (XSS) is a security vulnerability that allows attackers to inject malicious scripts into web pages viewed by users. Django’s template engine automatically escapes output to prevent XSS.

## SQL Injection
SQL injection is a serious security threat that allows attackers to execute malicious SQL queries on your database through your web application. Django, as a framework, provides built-in mechanisms to protect against such attacks.

## CSRF
CSRF (Cross-Site Request Forgery) token is an important security mechanism that protects your web applications from attacks that utilize forged requests. In Django, CSRF tokens are automatically embedded in forms and requests to protect against such attacks.

How the CSRF Token Works in Django
- Token Generation: When rendering an HTML page that contains a form, Django generates a unique CSRF token. This token is typically stored in the user's session and is added to each form as a hidden field.
- Including the Token in the Form: You can include the CSRF token in your templates by using {% csrf_token %}. This creates a hidden field containing the token, which the browser will send back to the server when the form is submitted.
- Server-Side Verification: When a user submits the form, Django automatically checks the CSRF token sent with the request. If the tokens do not match or the token is absent, Django rejects the request, triggering a CSRF error.
- Protection Against Attacks: By using the CSRF token, your application can verify that the request genuinely came from the authorized user and deny requests that may have been crafted by an external (malicious) site.