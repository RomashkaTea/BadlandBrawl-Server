# -*- coding: utf-8 -*-

from Utils.Writer import Writer


class OwnHomeData(Writer):

    def __init__(self, device):
        self.id = 24101
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeHexa('''0100007F6176B52000000001002483130000001F546F77657220436F6C6F723A204F766572646F7365206F66204F72616E67650890ABC8960C84A9F0960C90ABC8960C00000000000000000000001F546F77657220436F6C6F723A204F766572646F7365206F66204F72616E6765000000347B224261736531223A2231303132222C22436F6C6F72223A2223363630304646222C226C6F6F6B757056616C756573223A5B5D7D000084130000000E546F7765723A204D61646E65737308909592970C8493BA970C909592970C00000000000000000000000E546F7765723A204D61646E657373000000327B224261736531223A223139222C22436F6C6F72223A2223363630304646222C226C6F6F6B757056616C756573223A5B5D7D0000851300000020546F77657220436F6C6F723A204F7572204C6F726420616E6420536176696F720890FFDB970C84FD83980C90FFDB970C000000000000000000000020546F77657220436F6C6F723A204F7572204C6F726420616E6420536176696F72000000347B224261736531223A2231303238222C22436F6C6F72223A2223363630304646222C226C6F6F6B757056616C756573223A5B5D7D0000A9150000000F436F6C6F7373616C204672696461790380FC8F970CB8A59A970C80FC8F970C00000000000000000000000F436F6C6F7373616C204672696461790000003C7B22476C6F62616C4576656E744D6F6465223A223430222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D0000AA150000000F436F6C6F7373616C204672696461790380E6D9970CB88FE4970C80E6D9970C00000000000000000000000F436F6C6F7373616C204672696461790000003C7B22476C6F62616C4576656E744D6F6465223A223430222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D0000811A000000194576656E743A20426F6D6220427562626C65204D617968656D01A0DCF4960C90EAFE960C90A4F4960C0000000000000000000000194576656E743A20426F6D6220427562626C65204D617968656D000000387B22537572766976616C4D6F6465223A2232222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000BF1A0000001E476C6F62616C20426F6F73743A20446F6E6174696F6E20476F6C642078320380F0FA960CB8DF8F970C80F0FA960C00000000000000000000001E476C6F62616C20426F6F73743A20446F6E6174696F6E20476F6C642078320000003C7B22476C6F62616C4576656E744D6F6465223A223132222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D0000871B00000020476C6F62616C20426F6F73743A2054726962656D61746520426F6E7573202B320380C29A970CB8B1AF970C80C29A970C000000000000000000000020476C6F62616C20426F6F73743A2054726962656D61746520426F6E7573202B320000003C7B22476C6F62616C4576656E744D6F6465223A223130222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D00008F1B0000001D476C6F62616C20426F6F73743A20566963746F727920476F6C642078320380DAC4970CB8C9D9970C80DAC4970C00000000000000000000001D476C6F62616C20426F6F73743A20566963746F727920476F6C642078320000003B7B22476C6F62616C4576656E744D6F6465223A2230222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D0000941B00000020476C6F62616C20426F6F73743A2047656172204D756C7469706C6965722078320380ACE4970CB89BF9970C80ACE4970C000000000000000000000020476C6F62616C20426F6F73743A2047656172204D756C7469706C6965722078320000003C7B22476C6F62616C4576656E744D6F6465223A223337222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D0000A11B000000194C75636B79204461793A2048616C6C6F7765656E20456767730380E4E5960CB88DF0960C80E4E5960C0000000000000000000000194C75636B79204461793A2048616C6C6F7765656E20456767730000003C7B22476C6F62616C4576656E744D6F6465223A223239222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D0000A21B000000194C75636B79204461793A2048616C6C6F7765656E20456767730380CEAF970CB8F7B9970C80CEAF970C0000000000000000000000194C75636B79204461793A2048616C6C6F7765656E20456767730000003C7B22476C6F62616C4576656E744D6F6465223A223239222C22436F6C6F72223A2223464642413030222C226C6F6F6B757056616C756573223A5B5D7D00009A1C0000001D4F666665723A204368726973746D617320332028476966742045676729008882DA970C84F1EE970C8882DA970C00000000000000000000001D4F666665723A204368726973746D617320332028476966742045676729000002807B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F4348524953544D41535F33222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223730333130222C22546965723153686F704974656D223A223730333031222C22546965723253686F704974656D223A223730333032222C22546965723353686F704974656D223A223730333033222C22546965723453686F704974656D223A223730333035222C22546965723553686F704974656D223A223730333035222C22546965723653686F704974656D223A223730333037222C22546965723753686F704974656D223A223730333037222C22546965723853686F704974656D223A223730333130222C22546965723953686F704974656D223A223730333130222C2254696572313053686F704974656D223A223730333130222C2254696572313553686F704974656D223A223730333135222C2254696572323053686F704974656D223A223730333230222C2254696572353053686F704974656D223A223730333530222C2254696572363053686F704974656D223A223730333630222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000A11C0000002C4F666665723A20496E76616465722028556E7265616C20456767202B20436F726520496E76616465722031290088BADB960C84A9F0960C88BADB960C00000000000000000000002C4F666665723A20496E76616465722028556E7265616C20456767202B20436F726520496E76616465722031290000027C7B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F494E5641444552222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223830333130222C22546965723153686F704974656D223A223830333130222C22546965723253686F704974656D223A223830333130222C22546965723353686F704974656D223A223830333130222C22546965723453686F704974656D223A223830333130222C22546965723553686F704974656D223A223830333130222C22546965723653686F704974656D223A223830333130222C22546965723753686F704974656D223A223830333130222C22546965723853686F704974656D223A223830333130222C22546965723953686F704974656D223A223830333130222C2254696572313053686F704974656D223A223830333130222C2254696572313553686F704974656D223A223830333230222C2254696572323053686F704974656D223A223830333230222C2254696572353053686F704974656D223A223830333230222C2254696572363053686F704974656D223A223830333230222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000A21C000000244F666665723A2043686F636F6C6174652033202843686F636F6C617465204120456767290088C6F0960C84B585970C88C6F0960C0000000000000000000000244F666665723A2043686F636F6C6174652033202843686F636F6C61746520412045676729000002807B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F43484F434F4C4154455F33222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223732303130222C22546965723153686F704974656D223A223732303032222C22546965723253686F704974656D223A223732303032222C22546965723353686F704974656D223A223732303033222C22546965723453686F704974656D223A223732303035222C22546965723553686F704974656D223A223732303035222C22546965723653686F704974656D223A223732303037222C22546965723753686F704974656D223A223732303037222C22546965723853686F704974656D223A223732303130222C22546965723953686F704974656D223A223732303130222C2254696572313053686F704974656D223A223732303130222C2254696572313553686F704974656D223A223732303135222C2254696572323053686F704974656D223A223732303230222C2254696572353053686F704974656D223A223732303530222C2254696572363053686F704974656D223A223732303630222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000A31C000000164F666665723A2052756E65202852756E6520456767290088D285970C84C19A970C88D285970C0000000000000000000000164F666665723A2052756E65202852756E652045676729000002797B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F52554E45222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223830303032222C22546965723153686F704974656D223A223830303032222C22546965723253686F704974656D223A223830303032222C22546965723353686F704974656D223A223830303033222C22546965723453686F704974656D223A223830303035222C22546965723553686F704974656D223A223830303035222C22546965723653686F704974656D223A223830303037222C22546965723753686F704974656D223A223830303037222C22546965723853686F704974656D223A223830303130222C22546965723953686F704974656D223A223830303130222C2254696572313053686F704974656D223A223830303130222C2254696572313553686F704974656D223A223830303135222C2254696572323053686F704974656D223A223830303230222C2254696572353053686F704974656D223A223830303230222C2254696572363053686F704974656D223A223830303230222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000A41C000000184F666665723A205765656B2028556E7265616C20456767290088EAAF970C84D9C4970C88EAAF970C0000000000000000000000184F666665723A205765656B2028556E7265616C2045676729000002797B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F5745454B222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223738353130222C22546965723153686F704974656D223A223738353035222C22546965723253686F704974656D223A223738353035222C22546965723353686F704974656D223A223738353035222C22546965723453686F704974656D223A223738353035222C22546965723553686F704974656D223A223738353035222C22546965723653686F704974656D223A223738353037222C22546965723753686F704974656D223A223738353037222C22546965723853686F704974656D223A223738353130222C22546965723953686F704974656D223A223738353130222C2254696572313053686F704974656D223A223738353130222C2254696572313553686F704974656D223A223738353135222C2254696572323053686F704974656D223A223738353230222C2254696572353053686F704974656D223A223738353230222C2254696572363053686F704974656D223A223738353230222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000A51C000000204F666665723A20506F77657220342028537570657220506F77657220456767290088DE9A970C84CDAF970C88DE9A970C0000000000000000000000204F666665723A20506F77657220342028537570657220506F77657220456767290000027C7B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F504F5745525F34222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223738333230222C22546965723153686F704974656D223A223738333031222C22546965723253686F704974656D223A223738333032222C22546965723353686F704974656D223A223738333033222C22546965723453686F704974656D223A223738333035222C22546965723553686F704974656D223A223738333035222C22546965723653686F704974656D223A223738333037222C22546965723753686F704974656D223A223738333037222C22546965723853686F704974656D223A223738333130222C22546965723953686F704974656D223A223738333130222C2254696572313053686F704974656D223A223738333130222C2254696572313553686F704974656D223A223738333135222C2254696572323053686F704974656D223A223738333230222C2254696572353053686F704974656D223A223738333530222C2254696572363053686F704974656D223A223738333630222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000A61C000000344F666665723A2046617462756E6E795F3220284D7974686963616C20436C6F6E6520456767202B204D656368612042756E6E79290088F6C4970C84E5D9970C88F6C4970C0000000000000000000000344F666665723A2046617462756E6E795F3220284D7974686963616C20436C6F6E6520456767202B204D656368612042756E6E79290000027F7B224F766572726964654E616D65223A225449445F5350454349414C5F4F464645525F46415442554E4E595F32222C2253686F705370656E64657244617973496E416374697665223A33302C2253686F705370656E64657250657263656E74616765496E637265617365223A3130302C2253686F705370656E6465724361705765656B6C79223A66616C73652C2253686F705370656E6465724361704D6F6E74686C79223A747275652C2253686F705370656E646572436170416C6C54696D65223A66616C73652C225469657244656661756C7453686F704974656D223A223830373130222C22546965723153686F704974656D223A223830373035222C22546965723253686F704974656D223A223830373035222C22546965723353686F704974656D223A223830373035222C22546965723453686F704974656D223A223830373035222C22546965723553686F704974656D223A223830373035222C22546965723653686F704974656D223A223830373130222C22546965723753686F704974656D223A223830373130222C22546965723853686F704974656D223A223830373130222C22546965723953686F704974656D223A223830373130222C2254696572313053686F704974656D223A223830373130222C2254696572313553686F704974656D223A223830373230222C2254696572323053686F704974656D223A223830373230222C2254696572353053686F704974656D223A223830373530222C2254696572363053686F704974656D223A223830373530222C2254696572416C7465726E617469766573456E61626C6564223A66616C73652C22436F6C6F72223A2223343438393332222C226C6F6F6B757056616C756573223A5B5D7D0000B91C000000174576656E743A2053756464656E2044656174682028422901A096EA960C90A4F4960C90DEE9960C0000000000000000000000174576656E743A2053756464656E20446561746820284229000000397B22537572766976616C4D6F6465223A223139222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000861D0000001E4576656E743A20446F75626C65204D616E6120427562626C65205275736801A0D2D3970C90E0DD970C909AD3970C00000000000000000000001E4576656E743A20446F75626C65204D616E6120427562626C652052757368000000397B22537572766976616C4D6F6465223A223232222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D00008F1D000000174576656E743A20547269706C65204D616E61205275736801A0E889970C90F693970C90B089970C0000000000000000000000174576656E743A20547269706C65204D616E612052757368000000387B22537572766976616C4D6F6465223A2237222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000961D000000224576656E743A2032763220446F75626C65204D616E6120427562626C65205275736801A0BAA9970C90C8B3970C9082A9970C0000000000000000000000224576656E743A2032763220446F75626C65204D616E6120427562626C6520527573680000003A7B22537572766976616C4D6F6465223A22313533222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000981D000000164576656E743A20426C697A7A617264204D617968656D01A0C6BE970C90D4C8970C908EBE970C0000000000000000000000164576656E743A20426C697A7A617264204D617968656D000000397B22537572766976616C4D6F6465223A223130222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000A91D000000244576656E743A2032763220427261776C2042616C6C2028426C61737420526F636B65742901A080B4970C908EBE970C90C8B3970C0000000000000000000000244576656E743A2032763220427261776C2042616C6C2028426C61737420526F636B6574290000003A7B22537572766976616C4D6F6465223A22313439222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000B11D000000264576656E743A20466C79696E6720446F67676F73205370656369616C204368616C6C656E676501A0A2FF960C90B089970C90EAFE960C0000000000000000000000264576656E743A20466C79696E6720446F67676F73205370656369616C204368616C6C656E67650000003A7B22537572766976616C4D6F6465223A22313037222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000B21D0000001A4576656E743A2057696E73747265616B204368616C6C656E676501A0AE94970C9082A9970C90F693970C00000000000000000000001A4576656E743A2057696E73747265616B204368616C6C656E67650000003A7B22537572766976616C4D6F6465223A22313239222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000B51D000000244576656E743A20537469636B7920426F6D62205370656369616C204368616C6C656E676501A08CC9970C909AD3970C90D4C8970C0000000000000000000000244576656E743A20537469636B7920426F6D62205370656369616C204368616C6C656E67650000003A7B22537572766976616C4D6F6465223A22313132222C22436F6C6F72223A2223454334433243222C226C6F6F6B757056616C756573223A5B5D7D0000881E00000013456D6F6A69733A2048756E677279205061636B0780E4E5960CB8D3FA960C80E4E5960C000000000000000000000013456D6F6A69733A2048756E677279205061636B0000004F7B22456D6F6A6931223A223138222C22436F6C6F72223A2223434330304646222C22456D6F6A6932223A223736222C22456D6F6A6933223A223638222C226C6F6F6B757056616C756573223A5B5D7D0000891E00000011456D6F6A69733A2042697264205061636B0780F0FA960CB8DF8F970C80F0FA960C000000000000000000000011456D6F6A69733A2042697264205061636B000000507B22456D6F6A6931223A223634222C22436F6C6F72223A2223434330304646222C22456D6F6A6932223A22313033222C22456D6F6A6933223A223636222C226C6F6F6B757056616C756573223A5B5D7D00008A1E00000011456D6F6A69733A204769726C205061636B0780FC8F970CB8B1AF970C80FC8F970C000000000000000000000011456D6F6A69733A204769726C205061636B0000004F7B22456D6F6A6931223A223439222C22436F6C6F72223A2223434330304646222C22456D6F6A6932223A223838222C22456D6F6A6933223A223331222C226C6F6F6B757056616C756573223A5B5D7D00008B1E00000012456D6F6A69733A204D6F766965205061636B0780CEAF970CB8BDC4970C80CEAF970C000000000000000000000012456D6F6A69733A204D6F766965205061636B0000004E7B22456D6F6A6931223A2238222C22436F6C6F72223A2223434330304646222C22456D6F6A6932223A223736222C22456D6F6A6933223A223737222C226C6F6F6B757056616C756573223A5B5D7D00008C1E00000018456D6F6A69733A20537472696B657220426F79205061636B0780DAC4970CB8C9D9970C80DAC4970C000000000000000000000018456D6F6A69733A20537472696B657220426F79205061636B0000004E7B22456D6F6A6931223A2237222C22436F6C6F72223A2223434330304646222C22456D6F6A6932223A223734222C22456D6F6A6933223A223835222C226C6F6F6B757056616C756573223A5B5D7D0000982100000018456D6F6A69733A2048616C6C6F7765656E205061636B20320780E6D9970CB89BF9970C80E6D9970C000000000000000000000018456D6F6A69733A2048616C6C6F7765656E205061636B2032000000797B22456D6F6A6931223A223137222C22436F6C6F72223A2223434330304646222C22456D6F6A6932223A223136222C22456D6F6A6933223A223236222C22456D6F6A6934223A223834222C22456D6F6A6935223A223931222C22456D6F6A6936223A223836222C226C6F6F6B757056616C756573223A5B5D7D00008C290000000F42503A20416E6E6976657273617279058CB1A0960CA0EAFD970C8CB1A0960C00000000000000000000000F42503A20416E6E69766572736172790000005F7B22436F6C6F72223A2223636330306666222C22426174746C65706173734576656E744D6F6465223A223237222C22426174746C657061737353686F704974656D4964223A223730303238222C226C6F6F6B757056616C756573223A5B5D7D00009329000000244576656E743A204D656368612042756E6E79205370656369616C204368616C6C656E676501A098DE970C90ECF2970C90E0DD970C0000000000000000000000244576656E743A204D656368612042756E6E79205370656369616C204368616C6C656E67650000003A7B22436F6C6F72223A2223636330306666222C22537572766976616C4D6F6465223A22313433222C226C6F6F6B757056616C756573223A5B5D7D0002000000907B224944223A22434C414E5F4348455354222C22506172616D73223A7B22537461727454696D65223A223230313830363133543030303030302E3030305A222C224163746976654475726174696F6E223A225033645431316834356D222C22496E6163746976654475726174696F6E223A2250306454306831356D222C22436865737454797065223A5B2230225D7D7D0200000B467B224944223A2243524541544F525F434F444553222C22506172616D73223A7B22416374697665223A747275652C22436F646545787069726174696F6E223A3630343830302C2243616D706169676E45787069726174696F6E223A323539323030302C2243726561746F7273223A5B7B2243616D706169676E436F6465223A22424641222C2243726561746F72436F6465223A22424641222C2243726561746F724E616D65223A22424641227D2C7B2243616D706169676E436F6465223A224361707461696E54616C6962222C2243726561746F72436F6465223A224361707461696E54616C6962222C2243726561746F724E616D65223A224361707461696E54616C6962227D2C7B2243616D706169676E436F6465223A2243756D706947616D6572222C2243726561746F72436F6465223A2243756D706947616D6572222C2243726561746F724E616D65223A2243756D706947616D6572227D2C7B2243616D706169676E436F6465223A22446F634A617A79222C2243726561746F72436F6465223A22446F634A617A79222C2243726561746F724E616D65223A22446F634A617A79227D2C7B2243616D706169676E436F6465223A2246657263686F353032222C2243726561746F72436F6465223A2246657263686F353032222C2243726561746F724E616D65223A2246657263686F353032227D2C7B2243616D706169676E436F6465223A22477261706965222C2243726561746F72436F6465223A22477261706965222C2243726561746F724E616D65223A22477261706965227D2C7B2243616D706169676E436F6465223A224B6576696E693434222C2243726561746F72436F6465223A224B6576696E693434222C2243726561746F724E616D65223A224B6576696E693434227D2C7B2243616D706169676E436F6465223A226B6F6A696D616B616D6F222C2243726561746F72436F6465223A226B6F6A696D616B616D6F222C2243726561746F724E616D65223A226B6F6A696D616B616D6F227D2C7B2243616D706169676E436F6465223A224B7A5252222C2243726561746F72436F6465223A224B7A5252222C2243726561746F724E616D65223A224B7A5252227D2C7B2243616D706169676E436F6465223A224C656F706F6C64222C2243726561746F72436F6465223A224C656F706F6C64222C2243726561746F724E616D65223A224C656F706F6C64227D2C7B2243616D706169676E436F6465223A224D616C6361696465222C2243726561746F72436F6465223A224D616C6361696465222C2243726561746F724E616D65223A224D616C6361696465227D2C7B2243616D706169676E436F6465223A224D6F72616E31303031222C2243726561746F72436F6465223A224D6F72616E31303031222C2243726561746F724E616D65223A224D6F72616E31303031227D2C7B2243616D706169676E436F6465223A224E657279222C2243726561746F72436F6465223A224E657279222C2243726561746F724E616D65223A224E657279227D2C7B2243616D706169676E436F6465223A22536F6F72616A222C2243726561746F72436F6465223A22536F6F72616A222C2243726561746F724E616D65223A22536F6F72616A227D2C7B2243616D706169676E436F6465223A2256696F6C61222C2243726561746F72436F6465223A2256696F6C61222C2243726561746F724E616D65223A2256696F6C61227D2C7B2243616D706169676E436F6465223A22526165766F636F63222C2243726561746F72436F6465223A22526165766F636F63222C2243726561746F724E616D65223A22526165766F636F63227D2C7B2243616D706169676E436F6465223A226B6D616E7573222C2243726561746F72436F6465223A226B6D616E7573222C2243726561746F724E616D65223A226B6D616E7573227D2C7B2243616D706169676E436F6465223A22474454222C2243726561746F72436F6465223A22474454222C2243726561746F724E616D65223A22474454227D2C7B2243616D706169676E436F6465223A225365696E686F7239222C2243726561746F72436F6465223A225365696E686F7239222C2243726561746F724E616D65223A225365696E686F7239227D2C7B2243616D706169676E436F6465223A224A4D4A4450222C2243726561746F72436F6465223A224A4D4A4450222C2243726561746F724E616D65223A224A4D4A4450227D2C7B2243616D706169676E436F6465223A2248756E746168222C2243726561746F72436F6465223A2248756E746168222C2243726561746F724E616D65223A2248756E746168227D2C7B2243616D706169676E436F6465223A2253746566616E5456222C2243726561746F72436F6465223A2253746566616E5456222C2243726561746F724E616D65223A2253746566616E5456227D2C7B2243616D706169676E436F6465223A22576974687A79222C2243726561746F72436F6465223A22576974685A61636B222C2243726561746F724E616D65223A22576974685A61636B227D2C7B2243616D706169676E436F6465223A2253746F706465222C2243726561746F72436F6465223A2253746F706465222C2243726561746F724E616D65223A2253746F706465227D2C7B2243616D706169676E436F6465223A2247616D65737061696E222C2243726561746F72436F6465223A2247616D65737061696E222C2243726561746F724E616D65223A2247616D65737061696E227D2C7B2243616D706169676E436F6465223A22416C6578544D222C2243726561746F72436F6465223A22416C6578544D222C2243726561746F724E616D65223A22416C6578544D227D2C7B2243616D706169676E436F6465223A2252686F76617878222C2243726561746F72436F6465223A2252686F76617878222C2243726561746F724E616D65223A2252686F76617878227D2C7B2243616D706169676E436F6465223A22486F6C79436C6F6E79222C2243726561746F72436F6465223A22486F6C79436C6F6E79222C2243726561746F724E616D65223A22486F6C79436C6F6E79227D2C7B2243616D706169676E436F6465223A22536E69707578222C2243726561746F72436F6465223A2254657276616C65696A6F6E61222C2243726561746F724E616D65223A2254657276616C65696A6F6E61227D2C7B2243616D706169676E436F6465223A22436172736F6E4A6179222C2243726561746F72436F6465223A22436172736F6E4A6179222C2243726561746F724E616D65223A22436172736F6E4A6179227D2C7B2243616D706169676E436F6465223A2253616C616D616E6472616B65222C2243726561746F72436F6465223A2253414C222C2243726561746F724E616D65223A2253616C616D616E6472616B65227D2C7B2243616D706169676E436F6465223A224B324B222C2243726561746F72436F6465223A224B324B222C2243726561746F724E616D65223A224B324B227D2C7B2243616D706169676E436F6465223A226765726E69656E222C2243726561746F72436F6465223A224765726E69656E222C2243726561746F724E616D65223A224765726E69656E227D2C7B2243616D706169676E436F6465223A224E696E6A6158222C2243726561746F72436F6465223A224E696E6A6158222C2243726561746F724E616D65223A224E696E6A6158227D2C7B2243616D706169676E436F6465223A225249534849222C2243726561746F72436F6465223A225269736869222C2243726561746F724E616D65223A225269736869227D2C7B2243616D706169676E436F6465223A22426F6D626564222C2243726561746F72436F6465223A22426F6D626564222C2243726561746F724E616D65223A22426F6D626564227D2C7B2243616D706169676E436F6465223A225769746842726E222C2243726561746F72436F6465223A225769746842726E222C2243726561746F724E616D65223A225769746842726E227D5D7D7D00000000007F00000000000000007F0000000200301D9600AA237F0005081E3802137F7F7F7F087F7F7F7F7F000000087F7F7F7F7F000000087F7F7F7F7F000000087F7F7F7F7F00000000A4010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000A91D7F0000A91D00000000000000000000000000000000007F7FA21B1D80CEAF970CB8F7B9970CA21B11A901B601B101B901B801B401A401BB01B701BE01BD01B501BA0122BC01BF01A701118085F7950C80D98A970C80AD9E980C80C9B09A0C80F1D79C0C8099FF9E0C80C1A6A10C80E9CDA30C8091F5A50C80B99CA80C80E1C3AA0C8089EBAC0C80B192AF0C8093AFB10C8081E1B30C80A988B60C80D1AFB80C25850386038703880389038A038B038C038D038E038F039003910392039303940395039603970398039903A403A703AB03A503A8039A039E039F03A003A103A203AC03A603A903AA03AD03258083A69A0C8083A69A0C8083A69A0C80ABCD9C0C80ABCD9C0C80ABCD9C0C80D3F49E0C80D3F49E0C80D3F49E0C80FB9BA10C80FB9BA10C80FB9BA10C80A3C3A30C80A3C3A30C80A3C3A30C80CBEAA50C80CBEAA50C80CBEAA50C80F391A80C80F391A80C80F391A80C80DBFE970C8083A69A0C80ABCD9C0C80D3F49E0C80FB9BA10C80A5B7A40C80B99CA80C80B99CA80C80B99CA80C80B99CA80C80B99CA80C809BB9AA0C80C3E0AC0C80EB87AF0C8093AFB10C80BBD6B30C0729242A2B2C2D2E078083A69A0C80ABCD9C0C80D3F49E0C80FB9BA10C80A3C3A30C80CBEAA50C80F391A80C0A9F10A210A510A810AB10AE10B110B410B710BD100A80DBFE970C8083A69A0C80ABCD9C0C80D3F49E0C80FB9BA10C80A3C3A30C80CBEAA50C80F391A80C809BB9AA0C80C3E0AC0C050000000000050000000000053F8001810182018301050303020101050105050A0A050514283CB8018C291B8CC60800000001010000CE91E7E40D310200000000A41C0000ACC63FACC63F8FEBB8970C003DAECA09A9CA09A9CA09A9CA09A9CA09A9CA09ABCA09ABCA09AECA09AECA09AECA097F7F7F7FB3CA097F7F7F7FB8CA097F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7F7FB8CA097F7F7F7F7F7F7F7F7FB8CA091EA4010200000000000087D2B5970CA0D4B5970C0000B415007F007F7F000003020000B415000002011E01010001B4153200010013050000A00C0000010002B415901F0001001E010200A00C000003007F0F1E0000010100000000007F7F00380000010100000000007F7F00020000010100000000007F7F00130000010100000000007F7F00000003000004007F0300000C0400000300809423809423A0B5B7970C01020100000100000002027F0000000000007F000000007F007F7F007F00000000007F9C892B80DE348BE8B7970C00007F7F000200000400000000080000000000000000000000000000000100027F01007F000001017F000001027F000001037F000001047F000001057F000E02007F000002A80F7F000003010101010E7F0004020002040001000000000000000000000296F680030296F680030296F68003000000007FAB96B5970CAB96B5970C0000007F0000000000000000070381ADE204A40182ADE204A40197ADE20401000000028CADE2040490ADE20400049EA4E80300B8A4E8030082A4E8030093A4E8030000323200010100AB96B5970C0000000000000000007F7F7F7F7FC4959CFB06''')