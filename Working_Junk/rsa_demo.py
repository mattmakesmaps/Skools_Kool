__author__ = 'matt'

import rsa
(pubkey, privkey) = rsa.newkeys(368)
print pubkey, privkey