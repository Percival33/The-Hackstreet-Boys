// import React from 'react';
// import { Formik, Form as FormikForm } from 'formik';
// import styled from 'styled-components';
// import * as Yup from 'yup';
// import KodFormularza, { kodFormularzaValidationSchema } from './Inputs/KodFormularza';
// import WariantFormularza, { wariantFormularzaValidationSchema } from './Inputs/WariantFormularza';
// import CelZlozenia, { celZlozeniaValidationSchema } from './Inputs/CelZlozenia';
// import Data, { dataValidationSchema } from './Inputs/Data';
// import KodUrzedu, { kodUrzeduValidationSchema } from './Inputs/KodUrzedu';
// import Podmiot1, { podmiot1ValidationSchema } from './Inputs/Podmiot1';
// import OsobaFizyczna, { osobaFizycznaValidationSchema } from './Inputs/OsobaFizyczna';
// import AdresZamieszkaniaSiedziby, { adresZamieszkaniaSiedzibyValidationSchema } from './Inputs/AdresZamieszkaniaSiedziby';

// const validationSchema = Yup.object().shape({
//   ...kodFormularzaValidationSchema.fields,
//   ...wariantFormularzaValidationSchema.fields,
//   ...celZlozeniaValidationSchema.fields,
//   ...dataValidationSchema.fields,
//   ...kodUrzeduValidationSchema.fields,
//   ...podmiot1ValidationSchema.fields,
//   ...osobaFizycznaValidationSchema.fields,
//   ...adresZamieszkaniaSiedzibyValidationSchema.fields,
// });

// const StyledForm = styled(FormikForm)`
//   display: flex;
//   flex-direction: column;
//   gap: 20px;
//   padding: 20px;
//   border: 1px solid #ccc;
//   border-radius: 8px;
//   max-width: 400px;
//   margin: 50px auto;
//   background-color: #f9f9f9;
// `;

// const StyledButton = styled.button`
//   padding: 10px 20px;
//   background-color: #007bff;
//   color: white;
//   border: none;
//   border-radius: 4px;
//   cursor: pointer;
//   &:disabled {
//     background-color: #ccc;
//   }
// `;

// const MyForm = () => {
//   return (
//     <Formik
//       initialValues={{
//         kodSystemowy: 'PCC-3 (6)',
//         kodPodatku: 'PCC',
//         rodzajZobowiazania: 'Z',
//         wersjaSchemy: '1-0E',
//         wariantFormularza: 6,
//         celZlozenia: 1,
//         data: '2024-07-29',
//         kodUrzedu: '0271',
//         rola: 'Podatnik',
//         PESEL: '54121832134',
//         ImiePierwsze: 'KAMIL',
//         Nazwisko: 'WIRTUALNY',
//         DataUrodzenia: '1954-12-18',
//         rodzajAdresu: 'RAD',
//         KodKraju: 'PL',
//         Wojewodztwo: 'ŚLĄSKIE',
//         Powiat: 'M. KATOWICE',
//         Gmina: 'M. KATOWICE',
//         Ulica: 'ALPEJSKA',
//         NrDomu: '6',
//         NrLokalu: '66',
//         Miejscowosc: 'KATOWICE',
//         KodPocztowy: '66-666',
//       }}
//       validationSchema={validationSchema}
//       onSubmit={(values, { setSubmitting }) => {
//         console.log(values);
//         setSubmitting(false);
//       }}
//     >
//       {({ isSubmitting }) => (
//         <StyledForm>
//           <KodFormularza />
//           <WariantFormularza />
//           <CelZlozenia />
//           <Data />
//           <KodUrzedu />
//           <Podmiot1 />
//           <OsobaFizyczna />
//           <AdresZamieszkaniaSiedziby />
//           <StyledButton type="submit" disabled={isSubmitting}>
//             Submit
//           </StyledButton>
//         </StyledForm>
//       )}
//     </Formik>
//   );
// };

// export default MyForm;


// import React from 'react';
// import { Formik, Form as FormikForm } from 'formik';
// import styled from 'styled-components';
// import * as Yup from 'yup';
// import KodFormularza, { kodFormularzaValidationSchema } from './Inputs/KodFormularza';
// import WariantFormularza, { wariantFormularzaValidationSchema } from './Inputs/WariantFormularza';
// import CelZlozenia, { celZlozeniaValidationSchema } from './Inputs/CelZlozenia';
// import Data, { dataValidationSchema } from './Inputs/Data';
// import KodUrzedu, { kodUrzeduValidationSchema } from './Inputs/KodUrzedu';
// import Podmiot1, { podmiot1ValidationSchema } from './Inputs/Podmiot1';
// import OsobaFizyczna, { osobaFizycznaValidationSchema } from './Inputs/OsobaFizyczna';
// import AdresZamieszkaniaSiedziby, { adresZamieszkaniaSiedzibyValidationSchema } from './Inputs/AdresZamieszkaniaSiedziby';
// import PodmiotPart2, { podmiotValidationSchema } from './Inputs/Podmiot_part2';

// const validationSchema = Yup.object().shape({
//   ...kodFormularzaValidationSchema.fields,
//   ...wariantFormularzaValidationSchema.fields,
//   ...celZlozeniaValidationSchema.fields,
//   ...dataValidationSchema.fields,
//   ...kodUrzeduValidationSchema.fields,
//   ...podmiot1ValidationSchema.fields,
//   ...osobaFizycznaValidationSchema.fields,
//   ...adresZamieszkaniaSiedzibyValidationSchema.fields,
//   ...podmiotValidationSchema.fields,
// });

// const StyledForm = styled(FormikForm)`
//   display: flex;
//   flex-direction: column;
//   gap: 20px;
//   padding: 20px;
//   border: 1px solid #ccc;
//   border-radius: 8px;
//   max-width: 400px;
//   margin: 50px auto;
//   background-color: #f9f9f9;
// `;

// const StyledButton = styled.button`
//   padding: 10px 20px;
//   background-color: #007bff;
//   color: white;
//   border: none;
//   border-radius: 4px;
//   cursor: pointer;
//   &:disabled {
//     background-color: #ccc;
//   }
// `;

// const MyForm = props => {
//   return (
//     <Formik
//       initialValues={{
//         kodSystemowy: 'PCC-3 (6)',
//         kodPodatku: 'PCC',
//         rodzajZobowiazania: 'Z',
//         wersjaSchemy: '1-0E',
//         wariantFormularza: 6,
//         celZlozenia: 1,
//         data: '2024-07-29',
//         kodUrzedu: '0271',
//         rola: 'Podatnik',
//         PESEL: '54121832134',
//         ImiePierwsze: 'KAMIL',
//         Nazwisko: 'WIRTUALNY',
//         DataUrodzenia: '1954-12-18',
//         rodzajAdresu: 'RAD',
//         KodKraju: 'PL',
//         Wojewodztwo: 'ŚLĄSKIE',
//         Powiat: 'M. KATOWICE',
//         Gmina: 'M. KATOWICE',
//         Ulica: 'ALPEJSKA',
//         NrDomu: '6',
//         NrLokalu: '66',
//         Miejscowosc: 'KATOWICE',
//         KodPocztowy: '66-666',
//         p_7: '',
//         p_20: '',
//         p_21: '',
//         p_22: '',
//         p_23: '',
//         p_24: '',
//         p_25: '',
//         p_26: '',
//         p_27: '',
//         p_28: '',
//         p_29: '',
//         p_30: '',
//         p_31: '',
//         p_32: '',
//         p_33: '',
//         p_34: '',
//         p_35: '',
//         p_36: '',
//         p_37: '',
//         p_38: '',
//         p_39: '',
//         p_40: '',
//         p_41: '',
//         p_42: '',
//       }}
//       validationSchema={validationSchema}
//       onSubmit={(values, { setSubmitting }) => {
//         // console.log(values);
//         setSubmitting(false);
//       }}
//     >
//       {({ isSubmitting }) => (
//         <StyledForm>
//           <KodFormularza formObj={props.formObj}/>
//           <WariantFormularza formObj={props.formObj} />
//           <CelZlozenia  formObj={props.formObj}/>
//           <Data formObj={props.formObj}/>
//           <KodUrzedu formObj={props.formObj} />
//           <Podmiot1 formObj={props.formObj}/>
//           <OsobaFizyczna formObj={props.formObj}/>
//           <AdresZamieszkaniaSiedziby formObj={props.formObj} />
//           <PodmiotPart2 formObj={props.formObj}/>
//           <StyledButton type="submit" disabled={isSubmitting}>
//             Submit
//           </StyledButton>
//         </StyledForm>
//       )}
//     </Formik>
//   );
// };

// export default MyForm;

import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import styled from 'styled-components';

const StyledForm = styled(Form)`
  display: flex;
  flex-direction: column;
  gap: 10px;
  width:100%;
`;

const StyledField = styled(Field)`
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
`;

const StyledErrorMessage = styled(ErrorMessage)`
  color: red;
  font-size: 0.8em;
`;



const validationSchema = Yup.object({
  // czy_fizyczna: Yup.string().required('Required'),
  // data_urodzenia: Yup.date().required('Required'),
  // gmina: Yup.string().required('Required'),
  // ilosc_zalocznikow: Yup.number().required('Required'),
  // imie_pierwsze: Yup.string().required('Required'),
  // kod_pocztowy: Yup.string().required('Required'),
  // kod_urzedu_skarbowego: Yup.string().required('Required'),
  // kwota_do_zaplaty: Yup.number().required('Required'),
  // kwota_podatku: Yup.number().required('Required'),
  // miejsce_dokonania_czynnosci_prawnej: Yup.string().required('Required'),
  // miejsce_polozenia_rzeczy: Yup.string().required('Required'),
  // miejscowosc: Yup.string().required('Required'),
  // nazwisko: Yup.string().required('Required'),
  // nip: Yup.string().required('Required'),
  // nr_domu: Yup.string().required('Required'),
  // nr_lokalu: Yup.string().required('Required'),
  // obliczony_podatek_czynnosci_p1: Yup.number().required('Required'),
  // obliczony_podatek_czynnosci_p2: Yup.number().required('Required'),
  // opis_sytuacji: Yup.string().required('Required'),
  // pelna_nazwa: Yup.string().required('Required'),
  // pesel: Yup.string().required('Required'),
  // podmiot: Yup.string().required('Required'),
  // podstawa_opodatkowania_p1: Yup.number().required('Required'),
  // podstawa_opodatkowania_p2: Yup.number().required('Required'),
  // powiat: Yup.string().required('Required'),
  // procent_podatku: Yup.number().required('Required'),
  // przedmiot_opadatkowania: Yup.string().required('Required'),
  // skrocona_nazwa: Yup.string().required('Required'),
  // ulica: Yup.string().required('Required'),
  // wojewodztwo: Yup.string().required('Required'),
    czy_fizyczna: Yup.string().min(1, 'Must be at least 1 character long'),
  data_urodzenia: Yup.date().required('Required'),
  gmina: Yup.string().min(1, 'Must be at least 1 character long'),
  ilosc_zalocznikow: Yup.number().required('Required'),
  imie_pierwsze: Yup.string().min(1, 'Must be at least 1 character long'),
  kod_pocztowy: Yup.string().min(1, 'Must be at least 1 character long'),
  kod_urzedu_skarbowego: Yup.string().min(1, 'Must be at least 1 character long'),
  kwota_do_zaplaty: Yup.number().required('Required'),
  kwota_podatku: Yup.number().required('Required'),
  miejsce_dokonania_czynnosci_prawnej: Yup.string().min(1, 'Must be at least 1 character long'),
  miejsce_polozenia_rzeczy: Yup.string().min(1, 'Must be at least 1 character long'),
  miejscowosc: Yup.string().min(1, 'Must be at least 1 character long'),
  nazwisko: Yup.string().min(1, 'Must be at least 1 character long'),
  nip: Yup.string().min(1, 'Must be at least 1 character long'),
  nr_domu: Yup.string().min(1, 'Must be at least 1 character long'),
  nr_lokalu: Yup.string().min(1, 'Must be at least 1 character long'),
  obliczony_podatek_czynnosci_p1: Yup.number().required('Required'),
  obliczony_podatek_czynnosci_p2: Yup.number().required('Required'),
  opis_sytuacji: Yup.string().min(1, 'Must be at least 1 character long'),
  pelna_nazwa: Yup.string().min(1, 'Must be at least 1 character long'),
  pesel: Yup.string().min(1, 'Must be at least 1 character long'),
  podmiot: Yup.string().min(1, 'Must be at least 1 character long'),
  podstawa_opodatkowania_p1: Yup.number().required('Required'),
  podstawa_opodatkowania_p2: Yup.number().required('Required'),
  powiat: Yup.string().min(1, 'Must be at least 1 character long'),
  procent_podatku: Yup.number().required('Required'),
  przedmiot_opadatkowania: Yup.string().min(1, 'Must be at least 1 character long'),
  skrocona_nazwa: Yup.string().min(1, 'Must be at least 1 character long'),
  ulica: Yup.string().min(1, 'Must be at least 1 character long'),
  wojewodztwo: Yup.string().min(1, 'Must be at least 1 character long'),
});

const MyForm = (props) => {
  const initialValues = {
    czy_fizyczna: props.formObj.czy_fizyczna || '',
    data_urodzenia: props.formObj.data_urodzenia || '',
    gmina: props.formObj.gmina || '',
    ilosc_zalocznikow: props.formObj.ilosc_zalocznikow || 0,
    imie_pierwsze: props.formObj.imie_pierwsze || '',
    kod_pocztowy: props.formObj.kod_pocztowy || '',
    kod_urzedu_skarbowego: props.formObj.kod_urzedu_skarbowego || '',
    kwota_do_zaplaty: props.formObj.kwota_do_zaplaty || 0,
    kwota_podatku: props.formObj.kwota_podatku || 0,
    miejsce_dokonania_czynnosci_prawnej: props.formObj.miejsce_dokonania_czynnosci_prawnej || '',
    miejsce_polozenia_rzeczy: props.formObj.miejsce_polozenia_rzeczy || '',
    miejscowosc: props.formObj.miejscowosc || '',
    nazwisko: props.formObj.nazwisko || '',
    nip: props.formObj.nip || '',
    nr_domu: props.formObj.nr_domu || '',
    nr_lokalu: props.formObj.nr_lokalu || '',
    obliczony_podatek_czynnosci_p1: props.formObj.obliczony_podatek_czynnosci_p1 || 0,
    obliczony_podatek_czynnosci_p2: props.formObj.obliczony_podatek_czynnosci_p2 || 0,
    opis_sytuacji: props.formObj.opis_sytuacji || '',
    pelna_nazwa: props.formObj.pelna_nazwa || '',
    pesel: props.formObj.pesel || '',
    podmiot: props.formObj.podmiot || '',
    podstawa_opodatkowania_p1: props.formObj.podstawa_opodatkowania_p1 || 0,
    podstawa_opodatkowania_p2: props.formObj.podstawa_opodatkowania_p2 || 0,
    powiat: props.formObj.powiat || '',
    procent_podatku: props.formObj.procent_podatku || 0,
    przedmiot_opadatkowania: props.formObj.przedmiot_opadatkowania || '',
    skrocona_nazwa: props.formObj.skrocona_nazwa || '',
    ulica: props.formObj.ulica || '',
    wojewodztwo: props.formObj.wojewodztwo || '',
  };

 console.log('FORM ODSWIEZA SIE, PROPS:',props,props.formObj.nazwisko)
  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={(values, { setSubmitting }) => {
        console.log(values);
        setSubmitting(false);
      }}
    >
      
        <StyledForm>
          <label htmlFor="czy_fizyczna">Czy fizyczna</label>
          <StyledField type="text" name="czy_fizyczna" value={props.formObj.czy_fizyczna} />
          <StyledErrorMessage name="czy_fizyczna" component="div" />
  
          <label htmlFor="data_urodzenia">Data urodzenia</label>
          <StyledField type="date" name="data_urodzenia" value={props.formObj.data_urodzenia} />
          <StyledErrorMessage name="data_urodzenia" component="div" />
  
          <label htmlFor="gmina">Gmina</label>
          <StyledField type="text" name="gmina" value={props.formObj.gmina} />
          <StyledErrorMessage name="gmina" component="div" />
  
          <label htmlFor="ilosc_zalocznikow">Ilość załączników</label>
          <StyledField type="number" name="ilosc_zalocznikow" value={props.formObj.ilosc_zalocznikow} />
          <StyledErrorMessage name="ilosc_zalocznikow" component="div" />
  
          <label htmlFor="imie_pierwsze">Imię pierwsze</label>
          <StyledField type="text" name="imie_pierwsze" value={props.formObj.imie_pierwsze} />
          <StyledErrorMessage name="imie_pierwsze" component="div" />
  
          <label htmlFor="kod_pocztowy">Kod pocztowy</label>
          <StyledField type="text" name="kod_pocztowy" value={props.formObj.kod_pocztowy} />
          <StyledErrorMessage name="kod_pocztowy" component="div" />
  
          <label htmlFor="kod_urzedu_skarbowego">Kod urzędu skarbowego</label>
          <StyledField type="text" name="kod_urzedu_skarbowego" value={props.formObj.kod_urzedu_skarbowego} />
          <StyledErrorMessage name="kod_urzedu_skarbowego" component="div" />
  
          <label htmlFor="kwota_do_zaplaty">Kwota do zapłaty</label>
          <StyledField type="number" name="kwota_do_zaplaty" value={props.formObj.kwota_do_zaplaty} />
          <StyledErrorMessage name="kwota_do_zaplaty" component="div" />
  
          <label htmlFor="kwota_podatku">Kwota podatku</label>
          <StyledField type="number" name="kwota_podatku" value={props.formObj.kwota_podatku} />
          <StyledErrorMessage name="kwota_podatku" component="div" />
  
          <label htmlFor="miejsce_dokonania_czynnosci_prawnej">Miejsce dokonania czynności prawnej</label>
          <StyledField type="text" name="miejsce_dokonania_czynnosci_prawnej" value={props.formObj.miejsce_dokonania_czynnosci_prawnej} />
          <StyledErrorMessage name="miejsce_dokonania_czynnosci_prawnej" component="div" />
  
          <label htmlFor="miejsce_polozenia_rzeczy">Miejsce położenia rzeczy</label>
          <StyledField type="text" name="miejsce_polozenia_rzeczy" value={props.formObj.miejsce_polozenia_rzeczy} />
          <StyledErrorMessage name="miejsce_polozenia_rzeczy" component="div" />
  
          <label htmlFor="miejscowosc">Miejscowość</label>
          <StyledField type="text" name="miejscowosc" value={props.formObj.miejscowosc} />
          <StyledErrorMessage name="miejscowosc" component="div" />
  
          <label htmlFor="nazwisko">Nazwisko</label>
          <StyledField type="text" name="nazwisko" value={props.formObj.nazwisko} />
          <StyledErrorMessage name="nazwisko" component="div" />
  
          <label htmlFor="nip">NIP</label>
          <StyledField type="text" name="nip" value={props.formObj.nip} />
          <StyledErrorMessage name="nip" component="div" />
  
          <label htmlFor="nr_domu">Nr domu</label>
          <StyledField type="text" name="nr_domu" value={props.formObj.nr_domu} />
          <StyledErrorMessage name="nr_domu" component="div" />
  
          <label htmlFor="nr_lokalu">Nr lokalu</label>
          <StyledField type="text" name="nr_lokalu" value={props.formObj.nr_lokalu} />
          <StyledErrorMessage name="nr_lokalu" component="div" />
  
          <label htmlFor="obliczony_podatek_czynnosci_p1">Obliczony podatek czynności P1</label>
          <StyledField type="number" name="obliczony_podatek_czynnosci_p1" value={props.formObj.obliczony_podatek_czynnosci_p1} />
          <StyledErrorMessage name="obliczony_podatek_czynnosci_p1" component="div" />
  
          <label htmlFor="obliczony_podatek_czynnosci_p2">Obliczony podatek czynności P2</label>
          <StyledField type="number" name="obliczony_podatek_czynnosci_p2" value={props.formObj.obliczony_podatek_czynnosci_p2} />
          <StyledErrorMessage name="obliczony_podatek_czynnosci_p2" component="div" />
  
          <label htmlFor="opis_sytuacji">Opis sytuacji</label>
          <StyledField type="text" name="opis_sytuacji" value={props.formObj.opis_sytuacji} />
          <StyledErrorMessage name="opis_sytuacji" component="div" />
  
          <label htmlFor="pelna_nazwa">Pełna nazwa</label>
          <StyledField type="text" name="pelna_nazwa" value={props.formObj.pelna_nazwa} />
          <StyledErrorMessage name="pelna_nazwa" component="div" />
  
          <label htmlFor="pesel">PESEL</label>
          <StyledField type="text" name="pesel" value={props.formObj.pesel} />
          <StyledErrorMessage name="pesel" component="div" />
  
          <label htmlFor="podmiot">Podmiot</label>
          <StyledField type="text" name="podmiot" value={props.formObj.podmiot} />
          <StyledErrorMessage name="podmiot" component="div" />
  
          <label htmlFor="podstawa_opodatkowania_p1">Podstawa opodatkowania P1</label>
          <StyledField type="number" name="podstawa_opodatkowania_p1" value={props.formObj.podstawa_opodatkowania_p1} />
          <StyledErrorMessage name="podstawa_opodatkowania_p1" component="div" />
  
          <label htmlFor="podstawa_opodatkowania_p2">Podstawa opodatkowania P2</label>
          <StyledField type="number" name="podstawa_opodatkowania_p2" value={props.formObj.podstawa_opodatkowania_p2} />
          <StyledErrorMessage name="podstawa_opodatkowania_p2" component="div" />
  
          <label htmlFor="powiat">Powiat</label>
          <StyledField type="text" name="powiat" value={props.formObj.powiat} />
          <StyledErrorMessage name="powiat" component="div" />
  
          <label htmlFor="procent_podatku">Procent podatku</label>
          <StyledField type="number" name="procent_podatku" value={props.formObj.procent_podatku} />
          <StyledErrorMessage name="procent_podatku" component="div" />
  
          <label htmlFor="przedmiot_opadatkowania">Przedmiot opodatkowania</label>
          <StyledField type="text" name="przedmiot_opadatkowania" value={props.formObj.przedmiot_opadatkowania} />
          <StyledErrorMessage name="przedmiot_opadatkowania" component="div" />
  
          <label htmlFor="skrocona_nazwa">Skrócona nazwa</label>
          <StyledField type="text" name="skrocona_nazwa" value={props.formObj.skrocona_nazwa} />
          <StyledErrorMessage name="skrocona_nazwa" component="div" />
  
          <label htmlFor="ulica">Ulica</label>
          <StyledField type="text" name="ulica" value={props.formObj.ulica} />
          <StyledErrorMessage name="ulica" component="div" />
  
          <label htmlFor="wojewodztwo">Województwo</label>
          <StyledField type="text" name="wojewodztwo" value={props.formObj.wojewodztwo} />
          <StyledErrorMessage name="wojewodztwo" component="div" />
  
          {/* <StyledButton type="submit" >
            Submit
          </StyledButton> */}
        </StyledForm>
        {/* <StyledForm>
  <label htmlFor="czy_fizyczna">Czy fizyczna</label>
  <StyledField type="text" name="czy_fizyczna" />
  <StyledErrorMessage name="czy_fizyczna" component="div" />

  <label htmlFor="data_urodzenia">Data urodzenia</label>
  <StyledField type="date" name="data_urodzenia" />
  <StyledErrorMessage name="data_urodzenia" component="div" />

  <label htmlFor="gmina">Gmina</label>
  <StyledField type="text" name="gmina" />
  <StyledErrorMessage name="gmina" component="div" />

  <label htmlFor="ilosc_zalocznikow">Ilość załączników</label>
  <StyledField type="number" name="ilosc_zalocznikow" />
  <StyledErrorMessage name="ilosc_zalocznikow" component="div" />

  <label htmlFor="imie_pierwsze">Imię pierwsze</label>
  <StyledField type="text" name="imie_pierwsze" />
  <StyledErrorMessage name="imie_pierwsze" component="div" />

  <label htmlFor="kod_pocztowy">Kod pocztowy</label>
  <StyledField type="text" name="kod_pocztowy" />
  <StyledErrorMessage name="kod_pocztowy" component="div" />

  <label htmlFor="kod_urzedu_skarbowego">Kod urzędu skarbowego</label>
  <StyledField type="text" name="kod_urzedu_skarbowego" />
  <StyledErrorMessage name="kod_urzedu_skarbowego" component="div" />

  <label htmlFor="kwota_do_zaplaty">Kwota do zapłaty</label>
  <StyledField type="number" name="kwota_do_zaplaty" />
  <StyledErrorMessage name="kwota_do_zaplaty" component="div" />

  <label htmlFor="kwota_podatku">Kwota podatku</label>
  <StyledField type="number" name="kwota_podatku" />
  <StyledErrorMessage name="kwota_podatku" component="div" />

  <label htmlFor="miejsce_dokonania_czynnosci_prawnej">Miejsce dokonania czynności prawnej</label>
  <StyledField type="text" name="miejsce_dokonania_czynnosci_prawnej" />
  <StyledErrorMessage name="miejsce_dokonania_czynnosci_prawnej" component="div" />

  <label htmlFor="miejsce_polozenia_rzeczy">Miejsce położenia rzeczy</label>
  <StyledField type="text" name="miejsce_polozenia_rzeczy" />
  <StyledErrorMessage name="miejsce_polozenia_rzeczy" component="div" />

  <label htmlFor="miejscowosc">Miejscowość</label>
  <StyledField type="text" name="miejscowosc" />
  <StyledErrorMessage name="miejscowosc" component="div" />

  <label htmlFor="nazwisko">Nazwisko</label>
  <StyledField type="text" name="nazwisko" />
  <StyledErrorMessage name="nazwisko" component="div" />

  <label htmlFor="nip">NIP</label>
  <StyledField type="text" name="nip" />
  <StyledErrorMessage name="nip" component="div" />

  <label htmlFor="nr_domu">Nr domu</label>
  <StyledField type="text" name="nr_domu" />
  <StyledErrorMessage name="nr_domu" component="div" />

  <label htmlFor="nr_lokalu">Nr lokalu</label>
  <StyledField type="text" name="nr_lokalu" />
  <StyledErrorMessage name="nr_lokalu" component="div" />

  <label htmlFor="obliczony_podatek_czynnosci_p1">Obliczony podatek czynności P1</label>
  <StyledField type="number" name="obliczony_podatek_czynnosci_p1" />
  <StyledErrorMessage name="obliczony_podatek_czynnosci_p1" component="div" />

  <label htmlFor="obliczony_podatek_czynnosci_p2">Obliczony podatek czynności P2</label>
  <StyledField type="number" name="obliczony_podatek_czynnosci_p2" />
  <StyledErrorMessage name="obliczony_podatek_czynnosci_p2" component="div" />

  <label htmlFor="opis_sytuacji">Opis sytuacji</label>
  <StyledField type="text" name="opis_sytuacji" />
  <StyledErrorMessage name="opis_sytuacji" component="div" />

  <label htmlFor="pelna_nazwa">Pełna nazwa</label>
  <StyledField type="text" name="pelna_nazwa" />
  <StyledErrorMessage name="pelna_nazwa" component="div" />

  <label htmlFor="pesel">PESEL</label>
  <StyledField type="text" name="pesel" />
  <StyledErrorMessage name="pesel" component="div" />

  <label htmlFor="podmiot">Podmiot</label>
  <StyledField type="text" name="podmiot" />
  <StyledErrorMessage name="podmiot" component="div" />

  <label htmlFor="podstawa_opodatkowania_p1">Podstawa opodatkowania P1</label>
  <StyledField type="number" name="podstawa_opodatkowania_p1" />
  <StyledErrorMessage name="podstawa_opodatkowania_p1" component="div" />

  <label htmlFor="podstawa_opodatkowania_p2">Podstawa opodatkowania P2</label>
  <StyledField type="number" name="podstawa_opodatkowania_p2" />
  <StyledErrorMessage name="podstawa_opodatkowania_p2" component="div" />

  <label htmlFor="powiat">Powiat</label>
  <StyledField type="text" name="powiat" />
  <StyledErrorMessage name="powiat" component="div" />

  <label htmlFor="procent_podatku">Procent podatku</label>
  <StyledField type="number" name="procent_podatku" />
  <StyledErrorMessage name="procent_podatku" component="div" />

  <label htmlFor="przedmiot_opadatkowania">Przedmiot opodatkowania</label>
  <StyledField type="text" name="przedmiot_opadatkowania" />
  <StyledErrorMessage name="przedmiot_opadatkowania" component="div" />

  <label htmlFor="skrocona_nazwa">Skrócona nazwa</label>
  <StyledField type="text" name="skrocona_nazwa" />
  <StyledErrorMessage name="skrocona_nazwa" component="div" />

  <label htmlFor="ulica">Ulica</label>
  <StyledField type="text" name="ulica" />
  <StyledErrorMessage name="ulica" component="div" />

  <label htmlFor="wojewodztwo">Województwo</label>
  <StyledField type="text" name="wojewodztwo" />
  <StyledErrorMessage name="wojewodztwo" component="div" />

  <StyledButton type="submit">
    Submit
  </StyledButton>
</StyledForm> */}

    </Formik>
  )}

  export default MyForm;