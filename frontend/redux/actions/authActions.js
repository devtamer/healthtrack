import router from 'next/router';
import axios from 'axios';
import { AUTHENTICATE, DEAUTHENTICATE } from '../types';
import { API } from '../../config';
import { setCookie, removeCookie } from '../../utils/cookie';

// gets token from the api and stores it in the redux store and in cookie
const authenticate = ({ email, password }, type) => {
  // if (type !== 'login' && type !== 'signup') {
  //   throw new Error('Wrong API call!');
  // }
  return (dispatch) => {
    axios.post(`${API}/${type}`, { 'email': email, 'password': password })
      .then((response) => {
        console.log(response.data.auth_token);
        setCookie('token', response.data.auth_token);
        router.push('/dashboard');
        dispatch({ type: AUTHENTICATE, payload: response.data.auth_token });
      })
      .catch((err) => {
        console.log(err);
        throw new Error(err);
      });
  };
};
const patientRecords = ({ token }) => {
  {
    constresponse = axios.get(`${API}/records/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    }).then((response) => {
      return response.data;
    });
    console.log("response");
    return patients;

  }
}
const labOrders = ({ token }) => {
  return (dispatch) => {
    axios.get(`${API}/records/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    })
  }
}

// gets the token from the cookie and saves it in the store
const reauthenticate = (token) => {
  return (dispatch) => {
    dispatch({ type: AUTHENTICATE, payload: token });
  };
};

// removing the token
const deauthenticate = () => {
  return (dispatch) => {
    removeCookie('token');
    router.push('/');
    dispatch({ type: DEAUTHENTICATE });
  };
};


export default {
  authenticate,
  reauthenticate,
  deauthenticate,
  patientRecords,
  labOrders,

};

