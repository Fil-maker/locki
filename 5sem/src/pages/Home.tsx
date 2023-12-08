import MagnifierIcon from '../assets/simple-line-icons_magnifier.svg'
import BookIcon from '../assets/book.svg'
import UserIcon from '../assets/mingcute_user-info-fill.svg'
import CalculatorIcon from '../assets/bi_calculator-fill.svg'
import PageCard from '../components/PageCard'
import HouseIcon from '../assets/mdi_home-city.svg'
import RectsIcon from '../assets/rects.svg'

export default function Home() {
    return (
        <div>
            <h1 className="font-grtskmegabold text-white text-sm bg-cred h-20 py-7 pl-[250px]">БРУСНИКА</h1>
            <div className="mt-20 bg-clightestgrey border-clightergrey border-[1px] h-20" />
            <section className="grid grid-cols-3 gap-4 ml-[250px] mt-28 w-[1200px]">
                <div className="col-span-2 flex border-clightergrey border-[1px] py-5 rounded-md">
                    <div className='pr-5 pl-5 border-clightergrey border-r-[1px]'><img src={MagnifierIcon} /></div>
                    <input className='block w-full outline-none ml-7 mr-4' type="text" placeholder='Поиск' />
                </div>
                <div>
                    <button className='bg-cdarkergrey rounded-md text-sm text-white h-full w-48'>Найти</button>
                </div>
            </section>
            <section className='grid grid-cols-3 gap-4 ml-[250px] mt-12 w-[1200px]'>
                <PageCard image={BookIcon} ><div><p>положения</p><p>о подразделениях</p></div></PageCard>
                <PageCard image={UserIcon} ><div><p>должностные</p><p>инструкции</p></div></PageCard>
                <PageCard image={CalculatorIcon} imageWidth='w-24'><div><p>расчёты</p></div></PageCard>
                <PageCard image={HouseIcon} imageWidth='w-36'><div><p>информация</p><p>об объектах</p></div></PageCard>
                <PageCard image={RectsIcon} imageWidth='w-32'><div><p>материалы</p></div></PageCard>
                <PageCard><div><p>возможно, еще</p><p>какой-то пункт</p></div></PageCard>
            </section>
            <div className='mb-12'/>
        </div>
    )
}