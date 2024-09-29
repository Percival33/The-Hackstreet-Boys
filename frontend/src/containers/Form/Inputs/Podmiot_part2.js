// import React from 'react';
// import * as Yup from 'yup';
// import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

// export const podmiotValidationSchema = Yup.object().shape({
//   p_7: Yup.string().required('Podmiot składający deklarację is required'),
//   p_20: Yup.number().oneOf([1, 2, 3, 4], 'Invalid value for Przedmiot opodatkowania').required('Przedmiot opodatkowania is required'),
//   p_21: Yup.number().oneOf([1, 2], 'Invalid value for Miejsce położenia rzeczy').required('Miejsce położenia rzeczy is required'),
//   p_22: Yup.number().oneOf([1, 2], 'Invalid value for Miejsce dokonania czynności').required('Miejsce dokonania czynności is required'),
//   p_23: Yup.string().required('Zwięzłe określenie treści is required'),
//   p_24: Yup.number().required('Podstawa opodatkowania is required'),
//   p_25: Yup.number().required('Obliczony należny podatek is required'),
//   p_26: Yup.number().required('Podstawa opodatkowania is required'),
//   p_27: Yup.number().required('Obliczony należny podatek is required'),
//   p_28: Yup.number().required('Podstawa opodatkowania is required'),
//   p_29: Yup.number().required('Stawka podatku is required'),
//   p_30: Yup.number().required('Obliczony należny podatek is required'),
//   p_31: Yup.number().required('Podstawa opodatkowania is required'),
//   p_32: Yup.number().required('Stawka podatku is required'),
//   p_33: Yup.number().required('Obliczony należny podatek is required'),
//   p_34: Yup.number().required('Podstawa opodatkowania is required'),
//   p_35: Yup.number().required('Stawka podatku is required'),
//   p_36: Yup.number().required('Obliczony należny podatek is required'),
//   p_37: Yup.number().required('Podstawa opodatkowania is required'),
//   p_38: Yup.number().required('Stawka podatku is required'),
//   p_39: Yup.number().required('Obliczony należny podatek is required'),
//   p_40: Yup.number().required('Podstawa opodatkowania is required'),
//   p_41: Yup.number().required('Obliczony należny podatek is required'),
//   p_42: Yup.number().required('Obliczony należny podatek is required'),
//   p_43_a: Yup.string().required('Rodzaj czynności cywilnoprawnej is required'),
//   p_43: Yup.number().required('Podstawa opodatkowania is required'),
//   p_44: Yup.number().required('Stawka podatku is required'),
//   p_45: Yup.number().required('Obliczony należny podatek is required'),
//   p_46: Yup.number().required('Kwota należnego podatku is required'),
//   p_47: Yup.number().oneOf([1, 2], 'Invalid value for Typ spółki').required('Typ spółki is required'),
//   p_48: Yup.number().oneOf([1, 2, 3, 4, 5, 6, 7, 8], 'Invalid value for Podstawa opodatkowania dotyczy').required('Podstawa opodatkowania dotyczy is required'),
//   p_49: Yup.number().required('Podstawa opodatkowania is required'),
//   p_50: Yup.number().required('Opłaty i koszty is required'),
//   p_51: Yup.number().required('Podstawa obliczenia podatku is required'),
//   p_52: Yup.number().required('Kwota należnego podatku is required'),
//   p_53: Yup.number().required('Kwota podatku do zapłaty is required'),
// });

// const Podmiot = () => (
//   <div>
//     <label htmlFor="p_7">Podmiot składający deklarację</label>
//     <StyledField type="text" name="p_7" />
//     <StyledErrorMessage name="p_7" component="div" />

//     <label htmlFor="p_20">Przedmiot opodatkowania</label>
//     <StyledField type="number" name="p_20" />
//     <StyledErrorMessage name="p_20" component="div" />

//     <label htmlFor="p_21">Miejsce położenia rzeczy</label>
//     <StyledField type="number" name="p_21" />
//     <StyledErrorMessage name="p_21" component="div" />

//     <label htmlFor="p_22">Miejsce dokonania czynności</label>
//     <StyledField type="number" name="p_22" />
//     <StyledErrorMessage name="p_22" component="div" />

//     <label htmlFor="p_23">Zwięzłe określenie treści</label>
//     <StyledField type="text" name="p_23" />
//     <StyledErrorMessage name="p_23" component="div" />

//     <label htmlFor="p_24">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_24" />
//     <StyledErrorMessage name="p_24" component="div" />

//     <label htmlFor="p_25">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_25" />
//     <StyledErrorMessage name="p_25" component="div" />

//     <label htmlFor="p_26">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_26" />
//     <StyledErrorMessage name="p_26" component="div" />

//     <label htmlFor="p_27">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_27" />
//     <StyledErrorMessage name="p_27" component="div" />

//     <label htmlFor="p_28">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_28" />
//     <StyledErrorMessage name="p_28" component="div" />

//     <label htmlFor="p_29">Stawka podatku</label>
//     <StyledField type="number" name="p_29" />
//     <StyledErrorMessage name="p_29" component="div" />

//     <label htmlFor="p_30">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_30" />
//     <StyledErrorMessage name="p_30" component="div" />

//     <label htmlFor="p_31">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_31" />
//     <StyledErrorMessage name="p_31" component="div" />

//     <label htmlFor="p_32">Stawka podatku</label>
//     <StyledField type="number" name="p_32" />
//     <StyledErrorMessage name="p_32" component="div" />

//     <label htmlFor="p_33">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_33" />
//     <StyledErrorMessage name="p_33" component="div" />

//     <label htmlFor="p_34">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_34" />
//     <StyledErrorMessage name="p_34" component="div" />

//     <label htmlFor="p_35">Stawka podatku</label>
//     <StyledField type="number" name="p_35" />
//     <StyledErrorMessage name="p_35" component="div" />

//     <label htmlFor="p_36">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_36" />
//     <StyledErrorMessage name="p_36" component="div" />

//     <label htmlFor="p_37">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_37" />
//     <StyledErrorMessage name="p_37" component="div" />

//     <label htmlFor="p_38">Stawka podatku</label>
//     <StyledField type="number" name="p_38" />
//     <StyledErrorMessage name="p_38" component="div" />

//     <label htmlFor="p_39">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_39" />
//     <StyledErrorMessage name="p_39" component="div" />

//     <label htmlFor="p_40">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_40" />
//     <StyledErrorMessage name="p_40" component="div" />

//     <label htmlFor="p_41">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_41" />
//     <StyledErrorMessage name="p_41" component="div" />

//     <label htmlFor="p_42">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_42" />
//     <StyledErrorMessage name="p_42" component="div" />

//     <label htmlFor="p_43_a">Rodzaj czynności cywilnoprawnej</label>
//     <StyledField type="text" name="p_43_a" />
//     <StyledErrorMessage name="p_43_a" component="div" />

//     <label htmlFor="p_43">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_43" />
//     <StyledErrorMessage name="p_43" component="div" />

//     <label htmlFor="p_44">Stawka podatku</label>
//     <StyledField type="number" name="p_44" />
//     <StyledErrorMessage name="p_44" component="div" />

//     <label htmlFor="p_45">Obliczony należny podatek</label>
//     <StyledField type="number" name="p_45" />
//     <StyledErrorMessage name="p_45" component="div" />

//     <label htmlFor="p_46">Kwota należnego podatku</label>
//     <StyledField type="number" name="p_46" />
//     <StyledErrorMessage name="p_46" component="div" />

//     <label htmlFor="p_47">Typ spółki</label>
//     <StyledField type="number" name="p_47" />
//     <StyledErrorMessage name="p_47" component="div" />

//     <label htmlFor="p_48">Podstawa opodatkowania dotyczy</label>
//     <StyledField type="number" name="p_48" />
//     <StyledErrorMessage name="p_48" component="div" />

//     <label htmlFor="p_49">Podstawa opodatkowania</label>
//     <StyledField type="number" name="p_49" />
//     <StyledErrorMessage name="p_49" component="div" />

//     <label htmlFor="p_50">Opłaty i koszty</label>
//     <StyledField type="number" name="p_50" />
//     <StyledErrorMessage name="p_50" component="div" />

//     <label htmlFor="p_51">Podstawa obliczenia podatku</label>
//     <StyledField type="number" name="p_51" />
//     <StyledErrorMessage name="p_51" component="div" />

//     <label htmlFor="p_52">Kwota należnego podatku</label>
//     <StyledField type="number" name="p_52" />
//     <StyledErrorMessage name="p_52" component="div" />

//     <label htmlFor="p_53">Kwota podatku do zapłaty</label>
//     <StyledField type="number" name="p_53" />
//     <StyledErrorMessage name="p_53" component="div" />
//   </div>
// );

// export default Podmiot;
import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const podmiotValidationSchema = Yup.object().shape({
  p_7: Yup.string().required('Podmiot składający deklarację is required'),
  p_20: Yup.number().oneOf([1, 2, 3, 4], 'Invalid value for Przedmiot opodatkowania').required('Przedmiot opodatkowania is required'),
  p_21: Yup.number().oneOf([1, 2], 'Invalid value for Miejsce położenia rzeczy').nullable(),
  p_22: Yup.number().oneOf([1, 2], 'Invalid value for Miejsce dokonania czynności').nullable(),
  p_23: Yup.string().min(1, 'Minimum length is 1').max(3500, 'Maximum length is 3500').required('Zwięzłe określenie treści is required'),
  p_24: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_25: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_26: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_27: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_28: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_29: Yup.number().min(0, 'Minimum value is 0').max(100, 'Maximum value is 100').max(99999, 'Maximum value is 5 digits'),
  p_30: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_31: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_32: Yup.number().min(0, 'Minimum value is 0').max(100, 'Maximum value is 100').max(99999, 'Maximum value is 5 digits').max(1, 'Maximum value is 1 digit'),
  p_33: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_34: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_35: Yup.number().min(0, 'Minimum value is 0').max(100, 'Maximum value is 100').max(99999, 'Maximum value is 5 digits'),
  p_36: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_37: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_38: Yup.number().min(0, 'Minimum value is 0').max(100, 'Maximum value is 100').max(99999, 'Maximum value is 5 digits'),
  p_39: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_40: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_41: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits'),
  p_42: Yup.string().nullable(),
  p_43_a: Yup.string().min(1, 'Minimum length is 1').max(240, 'Maximum length is 240').required('Rodzaj czynności cywilnoprawnej is required'),
  p_43: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits').required('Podstawa opodatkowania is required'),
  p_44: Yup.number().min(0, 'Minimum value is 0').max(100, 'Maximum value is 100').max(99999, 'Maximum value is 5 digits').required('Stawka podatku is required'),
  p_45: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits').required('Obliczony należny podatek is required'),
  p_46: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits').required('Kwota należnego podatku is required'),
  p_47: Yup.number().oneOf([1, 2], 'Invalid value for Typ spółki').required('Typ spółki is required'),
  p_48: Yup.number().oneOf([1, 2, 3, 4, 5, 6, 7, 8], 'Invalid value for Podstawa opodatkowania dotyczy').required('Podstawa opodatkowania dotyczy is required'),
  p_49: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits').required('Podstawa opodatkowania is required'),
  p_50: Yup.number().min(0, 'Minimum value is 0').max(9999999999999999.99, 'Maximum value is 16 digits with 2 decimal places').required('Opłaty i koszty is required'),
  p_51: Yup.number().min(0, 'Minimum value is 0').max(9999999999999999.99, 'Maximum value is 16 digits with 2 decimal places').required('Podstawa obliczenia podatku is required'),
  p_52: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits').required('Kwota należnego podatku is required'),
  p_53: Yup.number().min(0, 'Minimum value is 0').max(99999999999999, 'Maximum value is 14 digits').required('Kwota podatku do zapłaty is required'),
});

const PodmiotPart2 = () => (
  <div>
    <label htmlFor="p_7">Podmiot składający deklarację</label>
    <StyledField type="text" name="p_7" />
    <StyledErrorMessage name="p_7" component="div" />

    <label htmlFor="p_20">Przedmiot opodatkowania</label>
    <StyledField type="number" name="p_20" />
    <StyledErrorMessage name="p_20" component="div" />

    <label htmlFor="p_21">Miejsce położenia rzeczy</label>
    <StyledField type="number" name="p_21" />
    <StyledErrorMessage name="p_21" component="div" />

    <label htmlFor="p_22">Miejsce dokonania czynności</label>
    <StyledField type="number" name="p_22" />
    <StyledErrorMessage name="p_22" component="div" />

    <label htmlFor="p_23">Zwięzłe określenie treści</label>
    <StyledField type="text" name="p_23" />
    <StyledErrorMessage name="p_23" component="div" />

    <label htmlFor="p_24">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_24" />
    <StyledErrorMessage name="p_24" component="div" />

    <label htmlFor="p_25">Obliczony należny podatek</label>
    <StyledField type="number" name="p_25" />
    <StyledErrorMessage name="p_25" component="div" />

    <label htmlFor="p_26">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_26" />
    <StyledErrorMessage name="p_26" component="div" />

    <label htmlFor="p_27">Obliczony należny podatek</label>
    <StyledField type="number" name="p_27" />
    <StyledErrorMessage name="p_27" component="div" />

    <label htmlFor="p_28">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_28" />
    <StyledErrorMessage name="p_28" component="div" />

    <label htmlFor="p_29">Stawka podatku</label>
    <StyledField type="number" name="p_29" />
    <StyledErrorMessage name="p_29" component="div" />

    <label htmlFor="p_30">Obliczony należny podatek</label>
    <StyledField type="number" name="p_30" />
    <StyledErrorMessage name="p_30" component="div" />

    <label htmlFor="p_31">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_31" />
    <StyledErrorMessage name="p_31" component="div" />

    <label htmlFor="p_32">Stawka podatku</label>
    <StyledField type="number" name="p_32" />
    <StyledErrorMessage name="p_32" component="div" />

    <label htmlFor="p_33">Obliczony należny podatek</label>
    <StyledField type="number" name="p_33" />
    <StyledErrorMessage name="p_33" component="div" />

    <label htmlFor="p_34">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_34" />
    <StyledErrorMessage name="p_34" component="div" />

    <label htmlFor="p_35">Stawka podatku</label>
    <StyledField type="number" name="p_35" />
    <StyledErrorMessage name="p_35" component="div" />

    <label htmlFor="p_36">Obliczony należny podatek</label>
    <StyledField type="number" name="p_36" />
    <StyledErrorMessage name="p_36" component="div" />

    <label htmlFor="p_37">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_37" />
    <StyledErrorMessage name="p_37" component="div" />

    <label htmlFor="p_38">Stawka podatku</label>
    <StyledField type="number" name="p_38" />
    <StyledErrorMessage name="p_38" component="div" />

    <label htmlFor="p_39">Obliczony należny podatek</label>
    <StyledField type="number" name="p_39" />
    <StyledErrorMessage name="p_39" component="div" />

    <label htmlFor="p_40">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_40" />
    <StyledErrorMessage name="p_40" component="div" />

    <label htmlFor="p_41">Obliczony należny podatek</label>
    <StyledField type="number" name="p_41" />
    <StyledErrorMessage name="p_41" component="div" />

    <label htmlFor="p_42">Obliczony należny podatek</label>
    <StyledField type="text" name="p_42" />
    <StyledErrorMessage name="p_42" component="div" />

    <label htmlFor="p_43_a">Rodzaj czynności cywilnoprawnej</label>
    <StyledField type="text" name="p_43_a" />
    <StyledErrorMessage name="p_43_a" component="div" />

    <label htmlFor="p_43">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_43" />
    <StyledErrorMessage name="p_43" component="div" />

    <label htmlFor="p_44">Stawka podatku</label>
    <StyledField type="number" name="p_44" />
    <StyledErrorMessage name="p_44" component="div" />

    <label htmlFor="p_45">Obliczony należny podatek</label>
    <StyledField type="number" name="p_45" />
    <StyledErrorMessage name="p_45" component="div" />

    <label htmlFor="p_46">Kwota należnego podatku</label>
    <StyledField type="number" name="p_46" />
    <StyledErrorMessage name="p_46" component="div" />

    <label htmlFor="p_47">Typ spółki</label>
    <StyledField type="number" name="p_47" />
    <StyledErrorMessage name="p_47" component="div" />

    <label htmlFor="p_48">Podstawa opodatkowania dotyczy</label>
    <StyledField type="number" name="p_48" />
    <StyledErrorMessage name="p_48" component="div" />

    <label htmlFor="p_49">Podstawa opodatkowania</label>
    <StyledField type="number" name="p_49" />
    <StyledErrorMessage name="p_49" component="div" />

    <label htmlFor="p_50">Opłaty i koszty</label>
    <StyledField type="number" name="p_50" />
    <StyledErrorMessage name="p_50" component="div" />

    <label htmlFor="p_51">Podstawa obliczenia podatku</label>
    <StyledField type="number" name="p_51" />
    <StyledErrorMessage name="p_51" component="div" />

    <label htmlFor="p_52">Kwota należnego podatku</label>
    <StyledField type="number" name="p_52" />
    <StyledErrorMessage name="p_52" component="div" />

    <label htmlFor="p_53">Kwota podatku do zapłaty</label>
    <StyledField type="number" name="p_53" />
    <StyledErrorMessage name="p_53" component="div" />
  </div>
);

export default PodmiotPart2;