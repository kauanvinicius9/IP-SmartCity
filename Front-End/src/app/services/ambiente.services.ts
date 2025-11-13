import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Ambiente } from '../models/ambiente';
import {environment} from '../../environments/environments';


@Injectable({
  providedIn: 'root'
})

export class AmbienteService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar():Observable<Ambiente[]> {
    const url = `${this.base}api/ambiente/`;
    return this.http.get<Ambiente[]>(url);

  }
}