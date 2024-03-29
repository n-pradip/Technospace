import React, { useState } from 'react'
import LogoImage from '../images/techno_space_logo.png'
import MobileMenuLinks from './MobileMenuLinks';
import { Link, useNavigate } from 'react-router-dom'
import { HiMenu } from "react-icons/hi";
import '../styles/component/Header.css'

const Header = () => {
    const navigate = useNavigate();
    const [mobileMenu, setMobileMenu] = useState(false);
    const [searchText, setSearchText] = useState('')
    const handleSubmit = (e) =>{
        e.preventDefault()
        navigate(`/search/${searchText}`)
    }

    return (
        <div className='w-full'>
            <nav className="header_container container mx-auto">
                <div className="grid grid-cols-2 lg:grid-cols-3 py-1">
                    <div className="box1 px-5 py-3 order-1 w-full flex text-left items-center">
                        <Link to='/' className="brand_name flex">
                            <img src={LogoImage} alt="" width="30px" height="auto" />
                            <p className="font-bold text-md items-base my-auto">Technospace(v2)</p>
                        </Link>
                    </div>
                    <form onSubmit={handleSubmit} className="box2 px-5 py-3 order-3 lg:order-2 col-span-2 lg:col-span-1 w-full flex items-center">
                        <input onChange={(e)=>{setSearchText(e.target.value)}} type="text" className="search_bar w-full px-3 py-[5px] text-sm" placeholder='Enter keyword here ...' />
                        <button to={`/search/${searchText}`} type="submit" className="search-button px-3 py-[5px] text-sm font-medium text-center text-white bg-[#07174D]">
                            Search
                        </button>
                    </form>
                    <div className="box3 order-2 px-5 py-3 lg:order-3 w-full flex justify-end items-center">
                        <div className="links hidden lg:block">
                            <ul className="grid grid-flow-col gap-5">
                                <li><Link to="/" className='font-[700] text-[18px] flex items-center gap-1' style={{ 'color': 'rgb(7,23,77)' }}>Home</Link></li>
                                <li><Link to="/bookmarks" className='font-[700] text-[18px] flex items-center gap-1' style={{ 'color': 'rgb(7,23,77)' }}>Bookmarks</Link></li>
                                <li><Link to="/login" className='font-[700] text-[18px] flex items-center gap-1' style={{ 'color': 'rgb(7,23,77)' }}>Login</Link></li>
                            </ul>
                        </div>
                        <div className="burger_menu block lg:hidden cursor-pointer" onClick={() => setMobileMenu(!mobileMenu)}>
                            <HiMenu size={30} />
                        </div>
                    </div>
                </div>
            </nav>
            {mobileMenu ?
                <div className="mobile_menu_container">
                    <MobileMenuLinks />
                </div>
                : null
            }
        </div>
    )
}

export default Header