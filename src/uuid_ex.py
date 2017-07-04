'''
Created on Jun 6, 2017

@author: maint
'''
import uuid 




def uuid2slug(uuidstring):
    return uuid.UUID(uuidstring).bytes.encode('base64').rstrip('=\n').replace('/', '_')


def slug2uuid(slug):
    return str(uuid.UUID(bytes=(slug + '==').replace('_', '/').decode('base64')))

def get_dns_domain_name(port_id):
    return 'www.'+uuid2slug(port_id)+'.com' 


def get_port_id(dns_domain_name):
    str_len = dns_domain_name.__len__()
    slug = dns_domain_name[4:str_len-4:] #remove prefix of 'www.' and suffix of '.com' - 4 chars each
    return slug2uuid(slug)

if __name__ == '__main__':
xx = uuid.uuid1()
print(xx)
dns = get_dns_domain_name(str(xx))
print(dns)
converted = get_port_id(dns)
print(converted)
print (converted == xx)


    