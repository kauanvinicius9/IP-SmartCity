import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Sensor } from '../models/sensor';
import {environment} from '../../environments/environments';


@Injectable({
  providedIn: 'root'
})

export class SensorService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar():Observable<Sensor[]> {
    const url = `${this.base}api/Sensor/`;
    return this.http.get<Sensor[]>(url);

  }
}