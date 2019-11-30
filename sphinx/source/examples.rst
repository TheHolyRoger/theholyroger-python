****************************
  Examples
****************************

A basic program that uses ``theholyroger-python`` looks like this:

First, import the library and exceptions.

::

    import theholyrogerrpc
    from theholyrogerrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``theholyroger`` instance of the current user on the local machine
with one call to
:func:`~theholyrogerrpc.connect_to_local`. This returns a :class:`~theholyrogerrpc.connection.TheHolyRogerConnection` objects:

::

    conn = theholyrogerrpc.connect_to_local()

Try to move one from account ``testaccount`` to account ``testaccount2`` using 
:func:`~theholyrogerrpc.connection.TheHolyRogerConnection.move`. Catch the :class:`~theholyrogerrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~theholyrogerrpc.connection.TheHolyRogerConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

