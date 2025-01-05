// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyA7yzeFkg5iRGlFcd2Jc9SA0MeLltGQ6_o",
    authDomain: "python4control-docs.firebaseapp.com",
    databaseURL: "https://python4control-docs-default-rtdb.firebaseio.com",
    projectId: "python4control-docs",
    storageBucket: "python4control-docs.appspot.com",
    messagingSenderId: "204322242506",
    appId: "1:204322242506:web:fbbfc490403f9840921933",
    measurementId: "G-HLVL8070EK"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const database = firebase.database();

export { database, ref, runTransaction }; 