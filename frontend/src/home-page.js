import React from 'react';
import ReactMarkdown from 'react-markdown';
import LeftTree from './left-tree';
import internalAPI from './utils/internal-api';

import './css/app.css';
import './css/github-markdown.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tree: {},
      curSelectedLeaf: {},
      markdownContent: '',
    }
  }

  componentDidMount() {
    internalAPI.getDocTree().then(res => {
      return this.setState({
        tree: res.data.doctree.children,
        curSelectedLeaf: res.data.doctree.children[0],  // README node
      })
    }).then(res => {
      let path = this.state.curSelectedLeaf.path;
      return internalAPI.getFileContentByPath(path);
    }).then(res => {
      this.setState({markdownContent: res.data.content});
    }).catch(err => {

    });
  }
  
  leafNodeClicked = (leafNode) => {
    this.setState({curSelectedLeaf: leafNode}, () => {
      internalAPI.getFileContentByPath(this.state.curSelectedLeaf.path).then(res => {
        this.setState({markdownContent: res.data.content});
      })
    });
  }

  render() {
    let { tree, markdownContent } = this.state;
    return (
      <div>
        <div className="top-bar"></div>
        <div className="main-content">
          <div className="column left-tree">
            <LeftTree
              tree={tree}
              leafNodeClicked={this.leafNodeClicked}
            />
          </div>
          <div className="column doc">
            <ReactMarkdown className="markdown-body" source={markdownContent}/>
          </div>
          <div className="column right-nav-bar">navbariii</div>
        </div>
        <div className="footer"></div>
      </div>
    )
  }
}

export default App;
