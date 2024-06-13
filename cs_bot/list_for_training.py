# Training data for the chatbot
list_for_training = [
                    "hello",
                    "Y'ello, my name is Bojo, MTN's customer service bot. How can i help you today?",

                     "good day",
                    "Y'ello, my name is Bojo, MTN's customer service bot. How can i help you today?",

                    "i can't receive calls",
                    "These are some simple tips on what to look out for if you do not receive calls;\n\n \n\n1. First Restart your phone\n2. Check if your SIM card is well placed in the phone\n3. Check your mobile network Settings or call settings\n4. Check if your SIM card is well placed in the phone\n5. Cancel all call diverts if any by dialing ##002#",

                    "i can't make calls",
                    "Ooops! Here are some steps to take if you can't make calls;\n\n1. Restart your phone,\n2. Check if your SIM card is well placed in the phone,\n3. Check your credit balance,\n4. Check your mobile network Settings or call settings,\n5. Top-up with airtime via MoMo if your last recharge date is over 90 days",

                    "what is mtn roaming bundle offers",
                    "MTN Roaming Bundle allows you to enjoy a discounted rate on outgoing calls, incoming calls, outgoing SMS and Data while roaming in selected destinations and partner networks.\nAll MTN Prepaid and Postpaid customers can subscribe to MTN Roaming Bundles.\n1. Dial *550#\n2. Select option 8 for More\n3. Select option 5 Roaming Offers",

                    "How do I send data to others using the myMTN App?",
                    "Download and launch the myMTN App. Select Buy/Send. Select Data. Choose the Data Amount. Select Others. Enter the recipient's number. Choose MoMo/Airtime for payment. Proceed to make payment.",
                    
                    "How do I send data to others using USSD?",
                    "Dial *321#. Select option 2 to proceed to Gift data.Follow the prompt. Enter the recipient's phone number and repeat it. Select the amount to purchase. Choose proceed.",

                    "How do I purchase mobile data bundle?",
                    "Buying mobile data bundle has been made easier using the following procedures:\n\nmyMTN App\n\nDownload myMTN App>Launch myMTN app > Select Buy/Send > Select Data > Select preferred data bundle > Select MoMo/Airtime as payment option\n\nUSSD\n\n1. Dial *138#\n2. Select 1 to proceed to buy bundle (No 4G bonus)\n3. Select option 1 to Buy Data Bundles\n4. Select option 1 or 2 to Buy For Self/Others\n5. Select preferred data bundle to purchase",

                    "How do I check my data bundle balance using the myMTN App?",
                    "To check your available data balance, follow these steps:\n1. Download myMTN App.\n2. Launch myMTN app.\n3. Select Data.",

                    "How do I check my data bundle balance using USSD?",
                    "To check your data bundle balance via USSD:\n1. Dial *323*4#.",

                    "I'm unable to connect to the internet, what do I do?",
                    "Here are some steps to follow to stay connected:\n1. Check your data balance by dialing *124# or using the MyMTN app.\n2. If no data bundles are available, dial *138# or use the MyMTN app to buy bundles.\n3. Ensure your mobile data connection is enabled.\n4. Open your web browser to see if the issue is app-specific or affects the entire internet.\n5. Restart your device if only some websites/apps work.\n6. Check your APN or Data settings if no websites/apps work.\n7. If others have the same issue, it may be a network problem. Try again later.\nIf the issue persists, contact us via our digital channels.",

                    "How do I check my data bundle balance using the myMTN App?",
                    "To check your available data balance, follow these steps:\n1. Download myMTN App.\n2. Launch myMTN app.\n3. Select Data.",

                    "How do I check my own number on my phone?",
                    "To check your own phone number, simply dial *156#, and select option My Number. Once this is done, a confirmation message will come back to your phone displaying your phone number. No fee is charged for this service.",

                    "What is MTN Family & Friends?",
                    "Family and friends is a call plan that allows you to choose up to 10 Family & Friends numbers (8 MTN numbers, 1 other network, and 1 international number) to enjoy lower call tariffs to registered numbers.",
    
                    "How do I subscribe MTN Family & Friends?",
                    "Simply follow this procedure below:\n1. Dial *550#\n2. Select option 8 for MORE\n3. Select option 6 to view family and friends Service\n4. Select option 1 to Add a number\n5. A confirmation SMS is sent after a successful add.",
    
                    "How do I check the numbers under my Family & Friends?",
                    "Want to check the numbers under your F & F?\n1. Dial *550#\n2. Select option 8 for MORE\n3. Select option 6 to view family and friends Service\n4. Select option 3 to check the numbers.",
    
                    "How do I remove a contact under Family & Friends?",
                    "Want to remove a contact? Here's how you can do that:\n1. Dial *550#\n2. Select option 8 for MORE\n3. Select option 6 to view family and friends Service\n4. Select option 2 to Remove a number\n5. A confirmation SMS is sent after the number is removed.",
    
                    "What are the benefits of MTN Family & Friends?",
                    "MTN Family & Friends allows you to make calls to registered numbers at a discounted rate.",

                    "What is MTN Caller Tunez?",
                    "MTN Caller Tunez allows customers to entertain their callers with music and other voice tones.",
    
                    "How do I subscribe to Caller Tunez?",
                    "Dial 1355 or *1355# and follow the prompts to subscribe to the Caller Tunez service.",
    
                    "What is Business Caller Tunez?",
                    "MTN Business Caller Tunez offers businesses an alternative advertising channel to put their message across directly to customers who call the phone lines of their staff members.",
    
                    "How do we subscribe to the business caller tunez?",
                    "Contact us via 0244308111 or mtnbusiness.GH@mtn.com to subscribe to Business Caller Tunez.",
    
                    "How much will I be charged for Caller Tunez subscription?",
                    "The charge for Caller Tunez is 0.65p for a monthly subscription and 0.26p for each song downloaded.",
    
                    "How do I unsubscribe from Caller Tunez?",
                    "Dial *1355# or send 'Unsub' to 1355 to unsubscribe from the service.",

                    "What is Xtratime or Xtrabyte?",
                    "Xtra time or Xtra byte allows you to borrow airtime or data and pay later at 10% commission.",

                    "How can I borrow data?",
                    "No need to worry about running out of data at odd times. We've got you covered with xtrabyte. Dial *506#, select option 4 Request a data advance, select preferred data and choose confirm/cancel service.",

                    "How do I activate xtratime?",
                    "Out of airtime. No need to fret! You can borrow airtime and pay later using these simple steps:\n1. Dial *506#\n2. Select Airtime options available\n3. Choose Confirm/Cancel service.",

                    "How do I change my MTN Nigeria tariff plan?", 
                    "You can change your tariff plan by dialing *406*1# and following the prompts.",

                    "What is MTN's official website?", 
                    "MTN Nigeria's official website is https://www.mtnonline.com/. Here, you can find information on products, services, and promotions.",

                    "How can I transfer airtime from my MTN line to another MTN number?", 
                    "To transfer airtime, dial *600*Recipient'sNumber*Amount*PIN# and follow the prompts. Your default PIN is 0000, but it's advisable to change it for security reasons.",

                    "What are the latest MTN data plans and their prices?", 
                    "MTN Nigeria offers a variety of data plans to suit your needs. You can dial *312*1# to view available data plans and their prices.",

                    "How do I recharge my MTN line?", 
                    "You can recharge your MTN line by purchasing airtime vouchers from vendors, using electronic top-up services, or via online platforms. You can also dial *311*PIN# to recharge using a voucher.",


]

# Training data for the chatbot
list_for_training2 = [
                    "hi",
                    "Y'ello, my name is Bojo, MTN's customer service bot. How can i help you today?",

                     "good morning",
                    "Y'ello, my name is Bojo, MTN's customer service bot. How can i help you today?",

                    "i'm unable to receive calls",
                    "These are some simple tips on what to look out for if you do not receive calls;\n\n \n\n1. First Restart your phone\n2. Check if your SIM card is well placed in the phone\n3. Check your mobile network Settings or call settings\n4. Check if your SIM card is well placed in the phone\n5. Cancel all call diverts if any by dialing ##002#",

                    "i'm unable to make calls",
                    "Ooops! Here are some steps to take if you can't make calls;\n\n1. Restart your phone,\n2. Check if your SIM card is well placed in the phone,\n3. Check your credit balance,\n4. Check your mobile network Settings or call settings,\n5. Top-up with airtime via MoMo if your last recharge date is over 90 days",

                    "mtn roaming bundle offers",
                    "MTN Roaming Bundle allows you to enjoy a discounted rate on outgoing calls, incoming calls, outgoing SMS and Data while roaming in selected destinations and partner networks.\nAll MTN Prepaid and Postpaid customers can subscribe to MTN Roaming Bundles.\n1. Dial *550#\n2. Select option 8 for More\n3. Select option 5 Roaming Offers",

                    "i want to send data on the mtn app",
                    "Download and launch the myMTN App. Select Buy/Send. Select Data. Choose the Data Amount. Select Others. Enter the recipient's number. Choose MoMo/Airtime for payment. Proceed to make payment.",
                    
                    "i want to send data",
                    "Dial *321#. Select option 2 to proceed to Gift data.Follow the prompt. Enter the recipient's phone number and repeat it. Select the amount to purchase. Choose proceed.",

                    "I want to buy data?",
                    "Buying mobile data bundle has been made easier using the following procedures:\n\nmyMTN App\n\nDownload myMTN App>Launch myMTN app > Select Buy/Send > Select Data > Select preferred data bundle > Select MoMo/Airtime as payment option\n\nUSSD\n\n1. Dial *138#\n2. Select 1 to proceed to buy bundle (No 4G bonus)\n3. Select option 1 to Buy Data Bundles\n4. Select option 1 or 2 to Buy For Self/Others\n5. Select preferred data bundle to purchase",

                    "i want to check my data balance",
                    "To check your data bundle balance via USSD:\n1. Dial *323*4#.",

                    "i can't browse the internet?",
                    "Here are some steps to follow to stay connected:\n1. Check your data balance by dialing *124# or using the MyMTN app.\n2. If no data bundles are available, dial *138# or use the MyMTN app to buy bundles.\n3. Ensure your mobile data connection is enabled.\n4. Open your web browser to see if the issue is app-specific or affects the entire internet.\n5. Restart your device if only some websites/apps work.\n6. Check your APN or Data settings if no websites/apps work.\n7. If others have the same issue, it may be a network problem. Try again later.\nIf the issue persists, contact us via our digital channels.",

                    "i want to check my data balance on my MTN app",
                    "To check your available data balance, follow these steps:\n1. Download myMTN App.\n2. Launch myMTN app.\n3. Select Data.",

                    "i want to check my phone number",
                    "To check your own phone number, simply dial *156#, and select option My Number. Once this is done, a confirmation message will come back to your phone displaying your phone number. No fee is charged for this service.",

                    "what is MTN Family and Friends?",
                    "Family and friends is a call plan that allows you to choose up to 10 Family & Friends numbers (8 MTN numbers, 1 other network, and 1 international number) to enjoy lower call tariffs to registered numbers.",
    
                    "i want to subscribe to  MTN Family and Friends?",
                    "Simply follow this procedure below:\n1. Dial *550#\n2. Select option 8 for MORE\n3. Select option 6 to view family and friends Service\n4. Select option 1 to Add a number\n5. A confirmation SMS is sent after a successful add.",
    
                    "i want to check the numbers under my Family & Friends?",
                    "Want to check the numbers under your F & F?\n1. Dial *550#\n2. Select option 8 for MORE\n3. Select option 6 to view family and friends Service\n4. Select option 3 to check the numbers.",
    
                    "How do I remove a mumber under Family & Friends?",
                    "Want to remove a contact? Here's how you can do that:\n1. Dial *550#\n2. Select option 8 for MORE\n3. Select option 6 to view family and friends Service\n4. Select option 2 to Remove a number\n5. A confirmation SMS is sent after the number is removed.",
    
                    "What are the benefits of MTN Family & Friends?",
                    "MTN Family & Friends allows you to make calls to registered numbers at a discounted rate.",

                    "what is MTN caller tunez?",
                    "MTN Caller Tunez allows customers to entertain their callers with music and other voice tones.",
    
                    "i want to activate caller tunez",
                    "Dial 1355 or *1355# and follow the prompts to subscribe to the Caller Tunez service.",
    
                    "What is business caller tunez?",
                    "MTN Business Caller Tunez offers businesses an alternative advertising channel to put their message across directly to customers who call the phone lines of their staff members.",
    
                    "i want to activate the business caller tunez?",
                    "Contact us via 0244308111 or mtnbusiness.GH@mtn.com to subscribe to Business Caller Tunez.",
    
                    "how much for caller tunez",
                    "The charge for Caller Tunez is 0.65p for a monthly subscription and 0.26p for each song downloaded.",
    
                    "i want to deactivate Caller Tunez?",
                    "Dial *1355# or send 'Unsub' to 1355 to unsubscribe from the service.",

                    "What is xtratime or xtrabyte?",
                    "Xtra time or Xtra byte allows you to borrow airtime or data and pay later at 10% commission.",

                    "i want to borrow data",
                    "No need to worry about running out of data at odd times. We've got you covered with xtrabyte. Dial *506#, select option 4 Request a data advance, select preferred data and choose confirm/cancel service.",

                    "i want to borrow airtime?",
                    "Out of airtime. No need to fret! You can borrow airtime and pay later using these simple steps:\n1. Dial *506#\n2. Select Airtime options available\n3. Choose Confirm/Cancel service.",

                    "i want to change my tariff plan?", 
                    "You can change your tariff plan by dialing *406*1# and following the prompts.",

                    "give me mtn website link", 
                    "MTN Nigeria's official website is https://www.mtnonline.com/. Here, you can find information on products, services, and promotions.",

                    "i want to send airtime", 
                    "To transfer airtime, dial *600*Recipient'sNumber*Amount*PIN# and follow the prompts. Your default PIN is 0000, but it's advisable to change it for security reasons.",

                    "give me data plans and their prices?", 
                    "MTN Nigeria offers a variety of data plans to suit your needs. You can dial *312*1# to view available data plans and their prices.",

                    "i want to recharge my number", 
                    "You can recharge your MTN line by purchasing airtime vouchers from vendors, using electronic top-up services, or via online platforms. You can also dial *311*PIN# to recharge using a voucher.",


]




