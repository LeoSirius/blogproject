import React from 'react';

import LeftTree from './left-tree';
import internalAPI from './utils/internal-api';

import './css/app.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tree: {},
    }
  }

  componentDidMount() {
    internalAPI.getDocTree().then(res => {
      this.setState({tree: res.data.doctree.children})
    }).catch(err => {

    });
  }

  render() {
    let { tree } = this.state;
    return (
      <div>
        <div className="top-bar"></div>
        <div className="main-content">
          <LeftTree
            tree={tree}
          />
          <div className="column doc">dovdoc</div>
          <div className="column right-nav-bar">navbariii</div>
        </div>
        <div className="footer"></div>
      </div>
    )
  }
}

export default App;
