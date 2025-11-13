import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Responsavel } from '../models/responsavel';
import {environment} from '../../environments/environments';


@Injectable({
  providedIn: 'root'
})

export class ResponsavelService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar():Observable<Responsavel[]> {
    const url = `${this.base}api/Responsavel/`;
    return this.http.get<Responsavel[]>(url);

  }
}