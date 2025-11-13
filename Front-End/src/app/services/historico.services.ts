import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Historico } from '../models/historico';
import {environment} from '../../environments/environments';


@Injectable({
  providedIn: 'root'
})

export class HistoricoService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar():Observable<Historico[]> {
    const url = `${this.base}api/historico/`;
    return this.http.get<Historico[]>(url);

  }
}