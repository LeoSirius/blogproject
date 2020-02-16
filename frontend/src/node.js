import React from 'react';

import Leaf from './leaf';


class Node extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isDisplayChildren: false,
    }
  }

  toggleDisplayChildren = (e) => {
    e.stopPropagation();
    this.setState({isDisplayChildren: !this.state.isDisplayChildren});
  }

  render() {
    let { node } = this.props;
    let { isDisplayChildren } = this.state;
    console.log(isDisplayChildren)
    return (
      <div className='node' onClick={this.toggleDisplayChildren}>
        {node.name}
        <div className={ isDisplayChildren ? '' :  'display-none'}>
        {node.children.map((node, index) => {
          if (node.hasOwnProperty('children')) {
            return (
              <Node key={node.name} node={node}/>
            )
          } else {
            return (
              <Leaf key={node.name} leaf={node}/>
            )
          }
        })}
        </div>
      </div>
    );
  }
}

export default Node;
