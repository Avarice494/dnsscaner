import asyncio
# 这是一个示例 Python 脚本。
import asyncio
import binascii
###############################基类##########################
from asyncio import transports
from time import sleep

dic = {
    "mssql_banner":"1201002f0000010000001a00060100200001020021000103002200040400260001ff00270000000000006401000000",
    "mssql_response":"ae00000003000b7300000000000000071404000000000000e003000020feffff040800005e000f007c000200800006008c0007009a000000000000009a000400a2000000a2000600000c29716d2e00000000ae00000000000000000000004400450053004b0054004f0050002d0033004d00560039004b0052004d0073006100b6a586a596a5e6a5f6a5c6a54e006100760069006300610074004f004400420043006d0061007300740065007200",
    "mssql_first":"1201002f0000010000001a00060100200001020021000103002200040400260001ff0027000000000000801a000000",
    "mssql_second":"1201010f000000001603010102010000fe03016125b5f701a36764b83fc6185c8d6a0377327caf3d3268e56ef01400bd9ea88c000018c014c0130035002fc00ac00900380032000a001300050004010000bd000a0006000400170018000b00020100002300a0387fd445e4d4ed840407a964738315d51e2b6fba6f0fa3272a38a9a5972378e26ef0797195252df682d75f1aa57dbb058bbee4eab6b17da17fec5bb396c482ad894efbb3d54388b8842e50d33991c5ea095d74f319a248227187fe849fc90eed0935b041429e63e242541306a7d1c3e7061128a668e57c244aad0e3c937d40fce686865aac7296abcfecd4bf121526d5ff5aedb7160e678904964029f898f07400170000ff01000100"
}
class BaseProtocol(asyncio.Protocol):
    def __init__(self, protocol='mysql', have_banner=False):
        self.protocol = protocol
        self.have_banner = have_banner
        self.username = ''
        self.passhash = ''
        self.remote_addr = ''
        self.remote_port = 0
        # self.logfile_obj = logfile
        self.have_data=False

    # def _save_pwd(self):
    #     queryip, country, area = get_ip_info(self.remote_addr)
    #     data = f'{self.protocol}::{get_now_str()}::{self.username}::{self.passhash}::{queryip}({country.strip()}_{area.strip()})\n'
    #     self.logfile_obj.write(data)
    #     self.logfile_obj.flush()

    def _get_banner(self):
        return b''

    def _parser_data(self, data):
        return b'', b''

    def _get_username(self, data, offset=0):
        return ''

    def _get_passwdhash(self, data, offset=0):
        return ''

    def _get_response(self):
        return b'this is response'

    def _get_bytes_by_flag(self, data, offset=0, endflag=0):
        ts = ''
        for t in data[offset:]:
            if t == endflag:
                break
            else:
                ts = ts + chr(t)
        return ts.encode('ascii'), len(ts)

    def connection_made(self, transport):
        self.transport = transport
        self.remote_addr, self.remote_port = transport.get_extra_info('socket').getpeername()
        # print(f'connection_made ,remote_addr:{self.remote_addr},remote_port:{self.remote_port}')
        if self.have_banner:
            self.transport.write(self._get_banner())

    def data_received(self, data):
        if len(data) > 3: self.have_data = True
        self._parser_data(data)
        self.transport.write(self._get_response())

    def connection_lost(self, exc):
        if self.have_data:self._save_pwd()

    def eof_received(self):
        pass


class ClientProtocol(BaseProtocol):
    def __init__(self, on_con_lost):
        self.count = 1
        self.on_con_lost = on_con_lost

    def connection_made(self, transport: transports.Transport) :
        self.remote_addr, self.remote_port=transport.get_extra_info('socket').getpeername()
        self.transport = transport
        self.transport.write(self._get_banner())

    def data_received(self, data: bytes) :
        self.transport.write(self._get_response())

    def _get_banner(self):
        a = dic["mssql_banner"]
        b = binascii.a2b_hex(a)
        return b

    def _get_response(self):
        a = dic["mssql_response"]
        b = binascii.a2b_hex(a)
        return b

    def connection_lost(self, exc):
        print('服务器连接断开')
        self.on_con_lost.set_result(True)


async def main():
    loop = asyncio.get_running_loop()
    on_con_lost = loop.create_future()

    transport, protocol = await loop.create_connection(lambda: ClientProtocol(on_con_lost),'192.168.231.110',9999)
    # 客户端用的是loop.create_connection
    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())