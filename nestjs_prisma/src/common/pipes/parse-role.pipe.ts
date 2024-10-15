/**
 * Here manually implemented pipes to validate the Role
 */
import {
  ArgumentMetadata,
  BadRequestException,
  Injectable,
  PipeTransform,
} from '@nestjs/common';
import { Role } from '@prisma/client';

@Injectable()
export class ParseRolePipe implements PipeTransform {
  transform(value: any, metadata: ArgumentMetadata): Role {
    if (!Object.values(Role).includes(value)) {
      console.log('Metadata', metadata);
      throw new BadRequestException(`Invalid role: ${value}`);
    }
    return value as Role;
  }
}
