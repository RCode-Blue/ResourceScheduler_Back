import React from 'react';

import { Calendar } from 'antd';

class Schedules extends React.Component {
  onPanelChange = (value, mode) => {
    console.log(value);
    console.log(mode);
  }

  onSelect = (value) => {
    console.log(value);
  }

  render() {
    return(
      <div>
        <Calendar onSelect={this.onSelect}/>
      </div>
    )
  }
}

export default Schedules;
