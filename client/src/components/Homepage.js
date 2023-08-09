import React from 'react'
import Sect from './Sect'
import Sect1 from './Sect1'
import Sect2 from './Sect2'
import Sect3 from './Sect3'



function Homepage() {
  return (
    <div>
   
    <Sect/>

    <br/>
    <div>
      <h2>Discover the Best Listings in the cities</h2>
      <p>Find the perfect rental home and comercial space to suit your need. Explore all available listings now.</p>
    </div> 
    <br/>
    
    <Sect1/>
    <br/>
    <div>
      <h2>Newest Listings</h2>
      <p>See the most up-to-date listings</p>
    </div> 
   
    
    <Sect2/>
    <br/>
    <h2>Featured Listings </h2>
    <p>We have a variaety of rental listings for renting in your area.</p>
    <Sect3/>


    </div>
  )
}

export default Homepage