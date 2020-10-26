# Twilio URL to Twilio CLI

This [Alfred](https://www.alfredapp.com/) workflow is for developers that uses a lot [Twilio](https://www.twilio.com/) and need to easily get data from the API with [Twilio CLI](https://www.twilio.com/docs/twilio-cli) when they are in [Twilio console](https://www.twilio.com/console).

## Why this workflow ?

Twilio CLI is a powerful tool, but there is a lot of ressources that you can work with, even if you usually use few of them.

This workflow allows you to get a ressource as a JSON object, simply by using Twilio console URL.

## Command
Just type `twilio` and paste the URL of the Twilio console page you are in.
This workflow will build Twilio CLI command, run it, and paste the result in your clipboard.

### Alternative action
You can use ⌘ if you simply want the command to be ran in a terminal window.

## Supported ressources

### Chat API
#### User
 - user : fetch a user
 - user's channels : fetch all the channel of a user
 
#### Channel
 - channel : fetch a channel
 - channel's members : fetch all the members of a channel
 - channel's messages : fetch all the messages of a channel

### Messages API
#### SMS
 - message : fetch a message

## Disclaimer
- Alfred only support Python 2.7 for now (which is the version that is shipped in macOS).
- I'm not a Python developer, this is my first ever script in this language. If you have any suggestion on the code, let me know, I'll be very happy to learn more about Python !
- This is my first published Alfred workflow
