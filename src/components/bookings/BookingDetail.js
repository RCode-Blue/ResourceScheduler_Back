import React from 'react';
import { Card } from 'antd';
import moment from 'moment';

const BookingDetails = (props) => {
// console.log(props);

// let start = moment(props.data.booking_start);
// console.log(moment(props.data.booking_start).format("LLLL"));

  return(
    <div>
      <Card title={props.data.title}>
        <p>{props.data.description}</p>
        <p>Resource: {props.data.resource_name}</p>
        <p>Start: {moment(props.data.booking_start).format("LLLL")}</p>
        <p>End: {moment(props.data.booking_end).format("LLLL")}</p>
      </Card>
    </div>
  )

}

export default BookingDetails;


