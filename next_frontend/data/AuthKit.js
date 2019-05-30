import axios from "axios";

const AUTH_TOKEN_KEY = "@AUTH_TOKEN";
const USER_ID_KEY = "@USER_ID";
const USER_EMAIL_KEY = "@USER_EMAIL";
const USER_FIRST_NAME_KEY = "@USER_FIRST_NAME";
const USER_LAST_NAME_KEY = "@USER_LAST_NAME";

export default class {
  constructor() {
    const baseURL = this._getBaseURL();
    const apiURL = this._getApiURL();
    this.authURL = `${baseURL}/api-token-auth/`;
    this.refreshURL = `${baseURL}/api-token-refresh/`;
    this.verifyURL = `${baseURL}/api-token-verify/`;
    this.registerURL = `${baseURL}/auth/users/`;
    this.activateURL = `${baseURL}/auth/users/confirm/`;
    this.acceptInviteURL = `${baseURL}/${apiURL}/accept-invitation/`;
    this.changePasswordURL = `${baseURL}/auth/password/`;
    this.resetPasswordURL = `${baseURL}/auth/password/reset/`;
    this.confirmResetPasswordURL = `${baseURL}/auth/password/reset/confirm`;
  }

  async auth(payload) {
    const response = await axios.post(this.authURL, payload);
    const token = response.data.token;
    this.setToken(token);
    return token;
  }

  async getMe() {
    const meURL = `/me/`;
    const response = await this.doGet(meURL);
    const data = response.data;

    localStorage.setItem(USER_ID_KEY, data.id);
    localStorage.setItem(USER_EMAIL_KEY, data.email);
    localStorage.setItem(USER_FIRST_NAME_KEY, data.first_name);
    localStorage.setItem(USER_LAST_NAME_KEY, data.last_name);

    return data;
  }

  getUserInfo() {
    if (process.browser) {
      return {
        id: localStorage.getItem(USER_ID_KEY),
        email: localStorage.getItem(USER_EMAIL_KEY),
        firstName: localStorage.getItem(USER_FIRST_NAME_KEY),
        lastName: localStorage.getItem(USER_LAST_NAME_KEY)
      };
    }
    return {};
  }

  verify(token) {
    return axios.post(this.verifyURL, { token });
  }

  refresh(token) {
    return axios.post(this.refreshURL, { token });
  }

  setToken(token) {
    return localStorage.setItem(AUTH_TOKEN_KEY, token);
  }

  getToken() {
    return localStorage.getItem(AUTH_TOKEN_KEY);
  }

  deleteToken() {
    return localStorage.removeItem(AUTH_TOKEN_KEY);
  }

  localStorageTokenIsValid() {
    const token = this.getToken();
    return this.verify(token);
  }

  async doGet(url, params) {
    const axios = await this.initializeAxiosInstance();
    const response = await axios.get(url);
    return response;
  }

  async doPut(url, payload) {
    const axios = await this.initializeAxiosInstance();
    const response = await axios.put(url, payload);
    return response;
  }

  async doPatch(url, payload) {
    const axios = await this.initializeAxiosInstance();
    const response = await axios.patch(url, payload);
    return response;
  }

  async doPost(url, payload) {
    const axios = await this.initializeAxiosInstance();
    const response = await axios.post(url, payload);
    return response;
  }

  async doDelete(url) {
    const axios = await this.initializeAxiosInstance();
    const response = await axios.delete(url);
    return response;
  }

  async verify_user() {
    return this.verify(this.getToken());
  }

  async refresh_user() {
    return this.refresh(this.getToken());
  }

  async initializeAxiosInstance() {
    if (
      this._instance &&
      this._instance.defaults.headers.common["Authorization"]
    ) {
      return this._instance;
    }

    this._instance = axios.create({
      baseURL: `${this._getBaseURL()}/${this._getApiURL()}`
    });

    if (process.browser) {
      const validTokenResponse = await this.localStorageTokenIsValid();
      if (validTokenResponse.data.token) {
        this._instance.defaults.headers.common["Authorization"] = `Bearer ${
          validTokenResponse.data.token
        }`;
      }
    }

    return this._instance;
  }

  async registerNewUser(userData) {
    return await axios.post(this.registerURL, userData);
  }

  async activateNewUser(uid, token) {
    return await axios.post(this.activateURL, { uid, token });
  }

  async acceptInvite(uid, token, newPassword) {
    return await axios.post(this.acceptInviteURL, { uid, token, newPassword });
  }

  async changePassword(password, newPassword, reNewPassword) {
    return await axios.post(this.changePasswordURL, {
      current_password: password,
      new_password: newPassword,
      re_new_password: reNewPassword
    });
  }

  async resetPassword(email) {
    return await axios.post(this.resetPasswordURL, { email });
  }

  async confirmResetPassword(uid, token, newPassword) {
    return await axios.post(this.confirmResetPasswordURL, {
      uid,
      token,
      newPassword
    });
  }

  arrayToObject(array) {
    return array.reduce((obj, item) => {
      obj[item.id] = item;
      return obj;
    }, {});
  }

  _getBaseURL() {
    return "http://hashimoto.willandskill.eu:8666"
  }

  _getApiURL() {
    return "api/v1";
  }
}
