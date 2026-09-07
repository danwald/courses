"use server";
import { z } from "zod";

const FontSchema = z.object({
  id: z.string(),
  customerId: z.string(),
  amount: z.number(),
  status: z.enum(["pending", "paid"]),
  date: z.string(),
});

const CreateInvoice = FontSchema.omit({ id: true, date: true });
export async function createInvoice(formData: FormData) {
  const { customerId, amount, status } = CreateInvoice.parse({
    customerId: formData.get("customerId"),
    amount: formData.get("amount"),
    status: formData.get("status"),
  });
}
