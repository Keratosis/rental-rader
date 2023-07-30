import React from 'react'
import Boxes from './Boxes'
import Sect from './Sect'
import Sect1 from './Sect1'
import Sect2 from './Sect2'
import Sect3 from './Sect3'



function Homepage() {
  return (
    <div>
    {/* <Boxes/>  */}
    <Sect/>

    <br/>
    <div>
      <h2>Discover the Best Properties in the cities</h2>
      <p>find the perfect rental home and comercial space. to suit your need explore all available listings now </p>
    </div> 
    <br/>
    
    <Sect1/>
    <br/>
    <p>we've recently added some new rental listings</p>
    
    <Sect2/>
    <br/>
    <p>Featured properties </p>
    we have a variaety of rantal properties for renting un your area
    <Sect3/>


    </div>
  )
}

export default Homepage