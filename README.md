# Project 2: Fintech Chatbot with Rasa Framework

Develop a chatbot using the Rasa framework that serves as a virtual assistant for users in the fintech industry.

This is a TEAM 6 group project

## Overview

The project rquires a Rasa server started using the command:

> rasa run actions actions.py file

other files that are edited toward the assignment goal are :

* nlu.yml, rules.yml, and stories.yml, all in the data directory
* config.yml, and domain.yml in the root direcory

## File Details

* actions.py
  The actions file has four primary purposes:
  * execution logic
  * dynamic content generation
  * slot setting and validation
  * triggering other actions or events
* nlu.yml
  NLU stands for natural language understanding (NLU). Primary purpose:
  * Intent recognition
  * Entity Extraction
  * Training data
  * Improved Understanding
* rules.yml
  Used for defining rules that determine how the chatbot should behave in specific situations.
  * Predefined Responsed
  * Handling FAQs
  * Form Actions
  * Fallback Mechanism
* stories.yml
  Used to define conversational paths that a chatbot can take.
  * Training Data for Dialogue Management
  * Sequential Flow
  * Context Handling
  * Branching Conversations
* config.yml
  Used to configure the behavior of the NLU component and dialogue management model
  * Pipeline Configuration
  * Policies Configuration
  * Model Training Settings
  * Language and Assistant Settings
* domain.yml
  Defining the enviorment in which your chatbot operates.
  * Intents and Entities
  * Responses
  * Actions

## Train the Model

Everytime we change one of the configuration files, we need to retrain the model.
This is done using

> rasa train

The training process is for training data for NLU and Core dialog management.
Pipeline management is controled throught the config.yml file.
The training learns from the specfied intents, entities, stories and rules.
It was in this file that we trained the model to respond to querries such as the balance in the savings or checking account.

## The Rasa Action Server

To start the system we use:

> rasa run actions

Runs custom actions such as external API calls, database queries, custom Python code, etc.
The action server listems at port 5055 so it does not conflict with the Rasa server, which listens at port 5005.

Whenever we modify the actions.yml, it may be neccesary to restart the action server in order for the changes to take effect.

In one of the scenarios presented below, the use wants to know their account balances.
We retrieve that information in a network call.
In the actions python file we have a class called

> ActionShowAccountBalance

There we use the jsonplaceholder to make a query and we used the returned jason data to similate
an account lookup, We use fields in the returend json to convert to saving and checking values

## Sample Output

To start the chatbot we run :

> rasa shell

Below is a sample conversation :

When the rasa shell starts we get a prompt:

> `Your input ->   `

Our reponse is "hello"

> `Your input ->  hello `
> `Welcome to the COP6481 Branch of the FinTech World Bank`
> `Your userid has been verified`
> `What would you like help with today? Your input ->`

Next we ask about out account:

> `Your input ->  account info`
> `Let me pull up that information for you...`
> `Account Info:`
> `Name: Leanne Graham`
> `Email: Sincere@april.biz`
> `Your input ->`

The bot makes a network call to get our account details
and presents that. Next we want to know what our balances are

> `Your input ->  balances`
> `Please specify which account you'd like to check: Checking or Savings?`
> `Your input ->`

The system recognizes that we have both a savings and a checking account and asks us
which account we are interested in inquiring about. we respond with checking

> `Your input ->  Checking`
> `Your checking account balance is: $3731.59.`
> `Your input ->`

The system displaus our checking account balance. Since we are already here,
lets find out our savings balance too.

> `Your input ->  savings`
> `Your savings account balance is: $12172.44.`
> `Your input ->`

next i am interested in what other account I can open

> `Your input ->  what additional accounts can I open ?`
> `We offer a variety of accounts to meet your needs:`
>
> `- Deposit Accounts`
> `- Investment Accounts`
> `- Credit Cards`
> `- Custodial Accounts`
> `- Business Account`

The system is able to process my natural language query, becasue
of the training, and lists the available accounts.
I am interested in opening a CD so I want to know more
about the Deposit Account

> `Your input ->  Deposit Accounts`
> `FinTech World Bank offers a wide variety of accounts beyond the standard savings and checking accounts.`
> `Here's a breakdown of the different categories and specific examples for  Deposit Accounts:`
>
> `- Certificates of Deposit (CDs): CDs offer a fixed interest rate for a set period, generally ranging from a few months to several years.`
>   `You receive a higher interest rate than a regular savings account in exchange for not being able to withdraw money before the term ends.`
> `- Money Market Accounts: These are similar to savings accounts but often have higher interest rates with certain requirements,`
>   `like minimum balances or limitations on withdrawals.`
> `- Individual Retirement Accounts (IRAs): These are tax-advantaged accounts designed for retirement savings.`
>   `There are Traditional IRAs, Roth IRAs, and variations with specific contribution and withdrawal rules.`
>   `Would you like additional information on opening an Account?`

The system describes the different deposit accounts in some detail and then asks if we would
like more information, We would so we respond in the affirmative.

> `Your input ->  yes`
> `To start the account opening process, please copy the following URL and paste it into your web browser's address bar:`
> `https://www.fintechworldbank.com/deposits/bank-cds/cd-accounts/`
> `Your input ->`

The system then provides the user with the url to get more information about opening a CD

---

---

---
