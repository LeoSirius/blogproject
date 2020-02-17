import axios from 'axios';
import FormData from 'form-data'

class InternalAPI {

  init() {
    this.req = axios.create();
    return this;
  }

  getDocTree() {
    const url = '/api/doctree/';
    return this.req.get(url);
  }

  getFileContentByPath(path) {
    const url = '/api/doc-content/' + encodeURIComponent(path) + '/';
    return this.req.get(url);
  }

}

let internalAPI = new InternalAPI();
internalAPI.init();

export default internalAPI;