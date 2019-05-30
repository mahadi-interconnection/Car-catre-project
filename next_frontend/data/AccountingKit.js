import AuthKit from "./AuthKit";

export default class {
  constructor() {
    this.url = "/accounting/";
    this.budgetinsight_url = "/budgetinsight/"
    this.authKit = new AuthKit();
  }

  getTransactionDetailUrl = id => `${this.url}transactions/${id}/`;

  async getTransactionList() {
    const url = `${this.url}transactions`;
    const response = await this.authKit.doGet(url);
    return response.data;
  }

  async getTransactionDetail(id) {
    const url = this.getTransactionDetailUrl(id);
    const response = await this.authKit.doGet(url);
    return response.data;
  }

  async patchTransaction(id, payload) {
    const url = this.getTransactionDetailUrl(id);
    const response = await this.authKit.doPatch(url, payload);
    return response.data;
  }

  async getCategoryList() {
    const url = `${this.url}categories`;
    const response = await this.authKit.doGet(url);
    return response.data;
  }

  async getCategoryDetail(id) {
    const url = this.getDetailUrl(id);
    const response = await this.authKit.doGet(url);
    return response.data;
  }

  async exchangeCodeForAccessToken(payload) {
    const url = `${this.budgetinsight_url}exchange-code-for-access-token/`;
    const response = await this.authKit.doPost(url, payload);
    return response.data;
  }

  async fetchAccounts() {
    const url = `${this.budgetinsight_url}fetch-accounts/`;
    const response = await this.authKit.doPost(url);
    return response.data;
  }

  async fetchTransactions() {
    const url = `${this.budgetinsight_url}fetch-transactions/`;
    const response = await this.authKit.doPost(url);
    return response.data;
  }

  async getAuthenticationUrl() {
    const url = `${this.budgetinsight_url}authentication-url/`;
    const response = await this.authKit.doGet(url);
    return response.data;
  }

  async getUserSettingsUrl() {
    const url = `${this.budgetinsight_url}user-settings-url/`;
    const response = await this.authKit.doGet(url);
    return response.data;
  }
}
