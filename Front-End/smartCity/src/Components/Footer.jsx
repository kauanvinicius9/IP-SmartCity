// Componente Footer com HTML semântico
import style from './Footer.module.css';

export default function Footer() {
    return(
        <footer className={style.footer}>
             &copy; {new Date().getFullYear()} Todos os direitos reservados
        </footer>
    );
}