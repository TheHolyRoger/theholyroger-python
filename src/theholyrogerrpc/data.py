# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
The Holy Roger RPC service, data objects.
"""
from theholyrogerrpc.util import DStruct


class ServerInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.getinfo`.

    - *errors* -- Number of errors.

    - *blocks* -- Number of blocks.

    - *paytxfee* -- Amount of transaction fee to pay.

    - *keypoololdest* -- Oldest key in keypool.

    - *genproclimit* -- Processor limit for generation.

    - *connections* -- Number of connections to other clients.

    - *difficulty* -- Current generating difficulty.

    - *testnet* -- True if connected to testnet, False if on real network.

    - *version* --The Holy Rogerclient version.

    - *proxy* -- Proxy configured in client.

    - *hashespersec* -- Number of hashes per second (if generation enabled).

    - *balance* -- Total current server balance.

    - *generate* -- True if generation enabled, False if not.

    - *unlocked_until* -- Timestamp (seconds since epoch) after which the wallet
                          will be/was locked (if wallet encryption is enabled).

    """


class AccountInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.listreceivedbyaccount`.

    - *account* -- The account of the receiving address.

    - *amount* -- Total amount received by the address.

    - *confirmations* -- Number of confirmations of the most recent transaction included.

    """


class AddressInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.listreceivedbyaddress`.

    - *address* -- Receiving address.

    - *account* -- The account of the receiving address.

    - *amount* -- Total amount received by the address.

    - *confirmations* -- Number of confirmations of the most recent transaction included.

    """


class TransactionInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.listtransactions`.

    - *account* -- account name.

    - *address* -- the address ROGERs were sent to, or received from.
    
    - *category* -- will be generate, send, receive, or move.

    - *amount* -- amount of transaction.

    - *fee* -- Fee (if any) paid (only for send transactions).

    - *confirmations* -- number of confirmations (only for generate/send/receive).

    - *txid* -- transaction ID (only for generate/send/receive).

    - *otheraccount* -- account funds were moved to or from (only for move).

    - *message* -- message associated with transaction (only for send).

    - *to* -- message-to associated with transaction (only for send).
    """


class AddressValidation(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.validateaddress`.

    - *isvalid* -- Validatity of address (:const:`True` or :const:`False`).

    - *ismine* -- :const:`True` if the address is in the server's wallet.

    - *address* --The Holy Rogeraddress.

    """


class WorkItem(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.getwork`.

    - *midstate* -- Precomputed hash state after hashing the first half of the data.

    - *data* -- Block data.

    - *hash1* -- Formatted hash buffer for second hash.

    - *target* -- Little endian hash target.

    """


class MiningInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.getmininginfo`.

    - *blocks* -- Number of blocks.

    - *currentblockweight* -- Weight of current block.

    - *currentblocktx* -- Number of transactions in current block.

    - *difficulty* -- Current generating difficulty.

    - *errors* -- Number of errors.

    - *generate* -- True if generation enabled, False if not.

    - *genproclimit* -- Processor limit for generation.

    - *hashespersec* -- Number of hashes per second (if generation enabled).

    - *networkhashps* -- Network hashes per second.

    - *pooledtx* -- Number of pooled transactions.

    - *chain* -- Testnet or mainnet network.

    - *warnings* -- Network warnings.

    """


class NetworkInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.getnetworkinfo`.

    - *version* -- the server version.

    - *subversion* -- the server version.

    - *protocolversion* -- the protocol version.

    - *localservices* -- the services we offer to the network.

    - *localrelay* -- true if transaction relay is requested from peers.

    - *timeoffset* -- the time offset.

    - *networkactive* -- whether p2p networking is enabled.

    - *connections* -- the number of connections.

    - *networks* -- information per network.

    - *relayfee* -- minimum relay fee for transactions in ROGER/kB.

    - *incrementalfee* -- minimum fee increment for mempool limiting or BIP 125 replacement in ROGER/kB.

    - *localaddresses* -- list of local addresses.

    - *errors* -- Number of errors.

    - *warnings* -- Number of warnings.

    """


class BlockchainInfo(DStruct):
    """
    Information object returned by :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.getblockchaininfo`.

    - *chain* -- current network name as defined in BIP70 (main, test, regtest).

    - *blocks* -- the current number of blocks processed in the server.

    - *headers* -- the current number of headers we have validated.

    - *bestblockhash* -- the hash of the currently best block.

    - *difficulty* -- the current difficulty.

    - *mediantime* -- median time for the current best block.

    - *verificationprogress* -- estimate of verification progress [0..1].

    - *initialblockdownload* -- estimate of whether this node is in Initial Block Download mode..

    - *chainwork* -- total amount of work in active chain, in hexadecimal.

    - *size_on_disk* -- the estimated size of the block and undo files on disk.

    - *pruned* -- if the blocks are subject to pruning.

    - *pruneheight* -- lowest-height complete block stored (only present if pruning is enabled).

    - *automatic_pruning* -- whether automatic pruning is enabled (only present if pruning is enabled).

    - *prune_target_size* -- the target size used by pruning (only present if automatic pruning is enabled).

    - *softforks* -- status of softforks in progress.

    - *bip9_softforks* -- status of BIP9 softforks in progress.

    - *errors* -- Number of errors.

    - *warnings* -- Number of warnings.

    """
