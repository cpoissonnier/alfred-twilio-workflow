import re
import sys
from abc import ABCMeta, abstractmethod

class Ressource:
    @abstractmethod
    def map_to_twilio_cli_command(self, url):
        pass

    @abstractmethod
    def get_twilio_cli_id(self):
        pass

    @abstractmethod
    def get_regex(self):
        pass

    def apply(self, url):
        return re.match(self.get_regex(), url)


class ChatUser(Ressource):
    def get_twilio_cli_id(self):
        return 'api:chat:v2:services:users:fetch'
    def get_regex(self):
        return r'https:\/\/www.twilio.com\/console\/chat\/services\/(\w+)\/users\/(\w+)$'
    def map_to_twilio_cli_command(self, url):
        match = re.search(self.get_regex(), url)
        return 'twilio {0} --service-sid {1} --sid {2} -o json'.format(self.get_twilio_cli_id(), match.group(1), match.group(2))


class ChatUserChannels(Ressource):
    def get_twilio_cli_id(self):
        return 'api:chat:v2:services:users:channels:list'
    def get_regex(self):
        return r'https:\/\/www.twilio.com\/console\/chat\/services\/(\w+)\/users\/(\w+)\/channels$'
    def map_to_twilio_cli_command(self, url):
        match = re.search(self.get_regex(), url)
        return 'twilio {0} --service-sid {1} --user-sid {2} -o json'.format(self.get_twilio_cli_id(), match.group(1), match.group(2))


class ChatChannel(Ressource):
    def get_twilio_cli_id(self):
        return 'api:chat:v2:services:channels:fetch'
    def get_regex(self):
        return r'https:\/\/www.twilio.com\/console\/chat\/services\/(\w+)\/channels\/(\w+)$'
    def map_to_twilio_cli_command(self, url):
        match = re.search(self.get_regex(), url)
        return 'twilio {0} --service-sid {1} --sid {2} -o json'.format(self.get_twilio_cli_id(), match.group(1), match.group(2))

class ChatChannelMembers(Ressource):
    def get_twilio_cli_id(self):
        return 'api:chat:v2:services:channels:members:list'
    def get_regex(self):
        return r'https:\/\/www.twilio.com\/console\/chat\/services\/(\w+)\/channels\/(\w+)\/members$'
    def map_to_twilio_cli_command(self, url):
        match = re.search(self.get_regex(), url)
        return 'twilio {0} --service-sid {1} --channel-sid {2} -o json'.format(self.get_twilio_cli_id(), match.group(1), match.group(2))

class ChatChannelMessages(Ressource):
    def get_twilio_cli_id(self):
        return 'api:chat:v2:services:channels:messages:list'
    def get_regex(self):
        return r'https:\/\/www.twilio.com\/console\/chat\/services\/(\w+)\/channels\/(\w+)\/messages$'
    def map_to_twilio_cli_command(self, url):
        match = re.search(self.get_regex(), url)
        return 'twilio {0} --service-sid {1} --channel-sid {2} -o json'.format(self.get_twilio_cli_id(), match.group(1), match.group(2))


class SmsMessage(Ressource):
    def get_twilio_cli_id(self):
        return 'api:core:messages:fetch'
    def get_regex(self):
        return r'https:\/\/www.twilio.com\/console\/sms\/logs\/(\w+)$'
    def map_to_twilio_cli_command(self, url):
        match = re.search(self.get_regex(), url)
        return 'twilio {0} --sid {1} -o json'.format(self.get_twilio_cli_id(), match.group(1))


query = sys.argv[1]

implementations = [ChatUser(), ChatUserChannels(), ChatChannel(), ChatChannelMembers(), ChatChannelMessages(), SmsMessage()]

implementations = filter(lambda implem: implem.apply(query), implementations)
command = (implementations[0] if implementations else None).map_to_twilio_cli_command(query)
sys.stdout.write(command)
sys.stdout.flush()
