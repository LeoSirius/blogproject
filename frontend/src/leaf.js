import React from 'react';

class Leaf extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  handleClick = (e) => {
    e.stopPropagation();
    this.props.leafNodeClicked(this.props.leaf);
  }

  render() {
    let { leaf } = this.props;
    return (
      <div className='leaf' onClick={this.handleClick}>
        {leaf.name}
      </div>
    );
  }
}

export default Leaf;
