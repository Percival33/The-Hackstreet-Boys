from generated.schemat import *
from src.application.form_serializer import FormSerializer
from src.domain.pcc3_declaration import PCC3Declaration
from xsdata.formats.dataclass.serializers import XmlSerializer as XMLSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

class XmlSerializer(FormSerializer):

	PERSON_FIELDS = ["pesel", "imie_pierwsze", "nazwisko", "data_urodzenia"]
	ADRESS_FIELDS = ["wojewodztwo", "powiat", "gmina", "ulica", "nr_domu", "nr_lokalu", "miejscowosc", "kod_pocztowy"]

	def serialize_pcc3(self, declaration: PCC3Declaration) -> str:
		mapped = self._map_domain_to_xml(declaration)
		serializer = XMLSerializer(config=SerializerConfig(pretty_print=True))
		return serializer.render(mapped).replace("ns0:", "").replace(":ns0", "")


	def _map_domain_to_xml(self, declaration: PCC3Declaration)->Deklaracja:
		header = self._get_header(declaration)
		person = Deklaracja.Podmiot1.OsobaFizyczna(**self._fields(declaration, self.PERSON_FIELDS))
		address = self._get_addr(declaration)
		return Deklaracja(header, Deklaracja.Podmiot1(person, None, address), self._get_details(declaration), Decimal(1))

	def _get_addr(self, declaration: PCC3Declaration) -> Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby:
		adr = TadresPolski(TadresPolskiKodKraju.PL, **self._fields(declaration, self.ADRESS_FIELDS))
		return Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby(adr)

	def _get_header(self, declaration: PCC3Declaration) -> Tnaglowek:
		us_code = TkodUs(declaration.kod_urzedu_skarbowego)
		return Tnaglowek(Tnaglowek.KodFormularza(TkodFormularza.PCC_3), TnaglowekWariantFormularza.VALUE_6, Tnaglowek.CelZlozenia(TcelZlozenia.VALUE_1), Tnaglowek.Data(XmlDate.today()), us_code)

	def _get_details(self, declaration: PCC3Declaration) -> Deklaracja.PozycjeSzczegolowe:
		p_fields = {
			"p_7": PozycjeSzczegoloweP7(declaration.podmiot),
			"p_20": PozycjeSzczegoloweP20(declaration.przedmiot_opadatkowania),
			"p_23": declaration.opis_sytuacji,
			"p_24": declaration.podstawa_opodatkowania_p1,
			"p_25": declaration.obliczony_podatek_czynnosci_p1,
			"p_46": declaration.kwota_podatku,
			"p_53": declaration.kwota_do_zaplaty,
			"p_62": declaration.ilosc_zalocznikow,
		}
		return Deklaracja.PozycjeSzczegolowe(**p_fields)

	def _fields(self, declaration: PCC3Declaration, fields: list[str]):
		return {x: declaration.__dict__[x] for x in declaration.__dict__ if x in fields}
