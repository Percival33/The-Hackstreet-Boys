from generated.schemat import *
from src.application.form_serializer import FormSerializer
from src.domain.pcc3_declaration import PCC3Declaration
from xsdata.formats.dataclass.serializers import XmlSerializer as XMLSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

class XmlSerializer(FormSerializer):

	PERSON_FIELDS = ["pesel", "imie_pierwsze", "nazwisko", "data_urodzenia"]
	COMPANY_FIELDS = ["NIP", "PelnaNazwa", "SkroconaNazwa"]
	ADRESS_FIELDS = ["wojewodztwo", "powiat", "gmina", "ulica", "nr_domu", "nr_lokalu", "miejscowosc", "kod_pocztowy"]

	def serialize_pcc3(self, declaration: PCC3Declaration) -> str:
		mapped = self._map_domain_to_xml(declaration)
		serializer = XMLSerializer(config=SerializerConfig(pretty_print=True))
		return serializer.render(mapped).replace("ns0:", "").replace(":ns0", "")


	def _map_domain_to_xml(self, declaration: PCC3Declaration)->Deklaracja:
		header = self._get_header(declaration)
		subject = self._get_subject(declaration)
		return Deklaracja(header, subject, self._get_details(declaration), Decimal(1))

	def _get_addr(self, declaration: PCC3Declaration) -> Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby:
		adr = TadresPolski(TadresPolskiKodKraju.PL, **self._fields(declaration, self.ADRESS_FIELDS))
		return Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby(adr)

	def _get_subject(self, declaration: PCC3Declaration) -> Deklaracja.Podmiot1:
		if declaration.czy_fizyczna:
			physcial, not_physical = Deklaracja.Podmiot1.OsobaFizyczna(**self._fields(declaration, self.PERSON_FIELDS)), None
		else:
			physcial, not_physical = None, TidentyfikatorOsobyNiefizycznej(**self._fields(declaration, self.COMPANY_FIELDS))
		address = self._get_addr(declaration)
		return Deklaracja.Podmiot1(physcial, not_physical, address)

	def _get_header(self, declaration: PCC3Declaration) -> Tnaglowek:
		us_code = TkodUs(declaration.kod_urzedu_skarbowego)
		try:
			y, m, d = declaration.data_dokonania_czynnosci.split('-', 2)
			date = XmlDate(int(y), int(m), int(d))
			if date < XmlDate(2024, 1, 1):
				date = XmlDate.today()
		except Exception:
			date = XmlDate.today()

		return Tnaglowek(Tnaglowek.KodFormularza(TkodFormularza.PCC_3), TnaglowekWariantFormularza.VALUE_6, Tnaglowek.CelZlozenia(TcelZlozenia.VALUE_1), Tnaglowek.Data(date), us_code)

	def _get_details(self, declaration: PCC3Declaration) -> Deklaracja.PozycjeSzczegolowe:
		p_fields = {
			"p_7": PozycjeSzczegoloweP7(declaration.podmiot),
			"p_20": PozycjeSzczegoloweP20(declaration.przedmiot_opadatkowania),
			"p_23": declaration.opis_sytuacji,
			"p_46": declaration.kwota_podatku,
			"p_54": declaration.wojewodztwo,
			"p_55": declaration.powiat,
			"p_56": declaration.gmina,
			"p_57": declaration.ulica,
			"p_58": declaration.nr_domu,
			"p_59": declaration.nr_lokalu,
			"p_60": declaration.miejscowosc,
			"p_61": declaration.kod_pocztowy,
			"p_53": declaration.kwota_do_zaplaty,
			"p_62": declaration.ilosc_zalocznikow,
		}
		if declaration.procent_podatku == "0.5":
			additional_fields = {
				"p_49": declaration.podstawa_opodatkowania_p05,
				"p_50": declaration.obliczony_podatek_czynnosci_p05,
			}
		elif declaration.procent_podatku == "2":
			additional_fields = {
				"p_26": declaration.podstawa_opodatkowania_p2,
				"p_27": declaration.obliczony_podatek_czynnosci_p2,
			}
		else:
			additional_fields = {
				"p_24": declaration.podstawa_opodatkowania_p1,
				"p_25": declaration.obliczony_podatek_czynnosci_p1,
			}

		p_fields.update(additional_fields)
		return Deklaracja.PozycjeSzczegolowe(**p_fields)

	def _fields(self, declaration: PCC3Declaration, fields: list[str]):
		return {x: declaration.__dict__[x] for x in declaration.__dict__ if x in fields}
