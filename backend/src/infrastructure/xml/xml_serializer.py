from generated.schemat import *
from src.application.form_serializer import FormSerializer
from src.domain.pcc3_declaration import PCC3Declaration
from xsdata.formats.dataclass.serializers import XmlSerializer as XMLSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

class XmlSerializer(FormSerializer):

	def serialize_pcc3(self, declaration: PCC3Declaration) -> str:
		mapped = self._map_domain_to_xml(declaration)
		serializer = XMLSerializer(config=SerializerConfig(pretty_print=True))
		return serializer.render(mapped).replace("ns0:", "").replace(":ns0", "")


	def _map_domain_to_xml(self, declaration: PCC3Declaration)->Deklaracja:
		#TODO write logic for mapping
		header = Tnaglowek(Tnaglowek.KodFormularza(TkodFormularza.PCC_3), TnaglowekWariantFormularza.VALUE_6, Tnaglowek.CelZlozenia(TcelZlozenia.VALUE_1), Tnaglowek.Data(XmlDate(2024, 1, 1)), TkodUs.VALUE_0213)
		person = Deklaracja.Podmiot1.OsobaFizyczna(pesel="75121968629", imie_pierwsze="Johny", nazwisko="Mielony", data_urodzenia="2023-12-31", imie_matki="Ania")
		adr = TadresPolski(TadresPolskiKodKraju.PL, "ŚLĄSKIE", "M. KATOWICE", "M. KATOWICE", "ALPEJSKA", "6", None, "KATOWICE", "66-666")
		addr = Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby(adr)
		z = Deklaracja.Podmiot1(person, None, addr)
		detail = Deklaracja.PozycjeSzczegolowe(p_7=PozycjeSzczegoloweP7.VALUE_1)
		return Deklaracja(header, z, detail, Decimal(1))
