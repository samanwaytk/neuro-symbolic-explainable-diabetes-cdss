import { useState } from "react";
import axios from "axios";

function PatientForm({ setResult }) {

  const [patient, setPatient] = useState({
    patient_name: "",
    gender: 1,
    age: 0,
    hypertension: 0,
    heart_disease: 0,
    smoking_history: 2,
    bmi: 0,
    HbA1c_level: 0,
    blood_glucose_level: 0
  });

  function handleChange(e) {

    setPatient({
      ...patient,
      [e.target.name]: e.target.value
    });

  }

  async function predict() {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        patient
      );

      setResult(response.data);

    } catch (error) {

      console.log(error);

    }

  }

  return (

    <div className="card">

      <h2>
        Patient Information
      </h2>

      <input
        name="patient_name"
        placeholder="Patient Name"
        onChange={handleChange}
      />

      <input
        name="age"
        type="number"
        placeholder="Age"
        onChange={handleChange}
      />

      <input
        name="bmi"
        type="number"
        placeholder="BMI"
        onChange={handleChange}
      />

      <input
        name="HbA1c_level"
        type="number"
        placeholder="HbA1c"
        onChange={handleChange}
      />

      <input
        name="blood_glucose_level"
        type="number"
        placeholder="Blood Glucose"
        onChange={handleChange}
      />

      <button onClick={predict}>
        Assess Diabetes Risk
      </button>

    </div>

  );
}

export default PatientForm;