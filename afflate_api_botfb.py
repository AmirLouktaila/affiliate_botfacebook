from botfb import *
#When you modify a project, you must call the modify function, otherwise it will not be modified
edit=EditBot('mybot')
#function create bot
create=CreateBot('mybot')
#here token
create.tokenFb("EAAN8ZATU4VNQBO6QG0JkfFv4hQXTyB2W6RlIvJ4nSN6xjwsZAbf4HJ2I25LavxSWiKOH9hAHVggHByJsZCxdnfwB1oD7DWfQjdlVNYhf9mmZBxl3LCI7PznUjW5nZARozOh8SRgRFajjt9aMXaOkHHVMRRLef9dPPiIY2myV3AA07EaKeWQOmuEclIDtMVJQq7ZCsZD","123456")
#here add any code for event
create.event(''' 
def mychat_fun(chat_me):
    from aliexpress_api import AliexpressApi, models
    aliexpress = AliexpressApi(appkey, secretkey, models.Language.EN, models.Currency.EUR, tracking_id)
    if "/start" in chat_me:

      reply ="""
  👋 مرحبًا بك في بوت   AliCoinsDz 
  
   مهمة هذا البوت زيادة نسبة التخفيض بالنقاط (العملات) 
   حسب المنتج 🔥 
  
  ✅ تعمل الروابط فقط مع المنتوجات التي يتوفر فيها تخفيض النقاط
  
          """

    else:
      def extract_links(text):
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        links = re.findall(url_pattern, text)
        return links

      input_text = chat_me
      links = extract_links(input_text)
      for link in links:
        try:

            affiliate_links = aliexpress.get_affiliate_links(link)
            reply =affiliate_links[0].promotion_link

        except Exception as e:
            affiliate_links = aliexpress.get_affiliate_links(link)
            reply=affiliate_links[0].promotion_link

  
    return reply



'''    )

create.getHost('a5c6-154-121-50-103.ngrok-free.app')
create.chatBot('chat_me','reply','mychat_fun')
create.runbot()
